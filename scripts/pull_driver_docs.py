#!/usr/bin/env python3
# Copyright (c) 2026 ADBC Drivers Contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Pull driver documentation from a GitHub releases and incorporate it into the
docs for that driver. This automates some fiddly parts of our docs updating
process.

Pre-requisites:

- Python
- gh CLI

Usage:
    python scripts/pull_driver_docs.py <repo_name> <release_tag>

Example:
    python scripts/pull_driver_docs.py mysql go/v0.5.0
"""

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional


def run_gh_api(endpoint: str) -> dict:
    """Run a GitHub API call using gh CLI."""
    result = subprocess.run(
        ["gh", "api", endpoint],
        capture_output=True,
        text=True,
        check=True,
    )
    return json.loads(result.stdout)


def download_asset(url: str, output_path: Path) -> None:
    """Download an asset from GitHub using gh CLI."""
    subprocess.run(
        ["gh", "api", url, "-H", "Accept: application/octet-stream"],
        capture_output=False,
        stdout=output_path.open("wb"),
        check=True,
    )


def check_repo_exists(repo_org: str, repo_name: str) -> bool:
    """Check if a repository exists and is accessible."""
    try:
        run_gh_api(f"repos/{repo_org}/{repo_name}")
        return True
    except subprocess.CalledProcessError:
        return False


def find_release(repo_org: str, repo_name: str, tag: str) -> Optional[dict]:
    """Find a release by tag. Importantly, includes drafts because we want to be
    able to preview docs before we publish the release.."""
    # First try the specific tag
    try:
        release = run_gh_api(f"repos/{repo_org}/{repo_name}/releases/tags/{tag}")
        return release
    except subprocess.CalledProcessError:
        pass

    # If not found, check all releases including drafts
    try:
        releases = run_gh_api(f"repos/{repo_org}/{repo_name}/releases")
        for release in releases:
            if release["tag_name"] == tag:
                return release
    except subprocess.CalledProcessError:
        # Could be repo doesn't exist or no releases
        pass

    return None


def extract_version_from_tag(tag: str) -> str:
    """Extract version string from tag (e.g., 'go/v0.5.0' -> 'v0.5.0')."""
    parts = tag.split("/")
    return parts[-1]


def get_all_versions_from_filesystem(driver_dir: Path) -> list[str]:
    """Get list of all version files in driver directory, sorted newest to
    oldest. We do this because we treat what's on the filesystem as truth for
    "what versions have been published for this driver".

    Matches version files like v0.5.0, v1.0.0-rc1, v2.3.4-beta.2, etc.
    """
    versions = []
    for file in driver_dir.glob("v*.md"):
        # Match v1.2.3 with optional pre-release suffix like -rc1, -beta.2, etc.
        if file.stem.startswith("v") and re.match(r"^v\d+\.\d+\.\d+", file.stem):
            versions.append(file.stem)

    # Sort by semantic version (newest first)
    def version_key(v: str) -> tuple:
        # Extract just the numeric part for sorting (v1.2.3-rc1 -> 1.2.3)
        match = re.match(r"^v(\d+)\.(\d+)\.(\d+)", v)
        if match:
            return tuple(int(p) for p in match.groups())
        return (0, 0, 0)  # Fallback for malformed versions

    return sorted(versions, key=version_key, reverse=True)


def build_toc_section(versions: list[str]) -> list[str]:
    """Build TOC section from list of versions."""
    toc_lines = [
        ":::{toctree}",
        ":maxdepth: 1",
        ":hidden:",
        "",
        "Changelog <changelog.md>",
    ]

    for version in versions:
        toc_lines.append(f"{version} <{version}.md>")

    toc_lines.extend([":::", ""])

    return toc_lines


def build_previous_versions_section(
    versions: list[str], current_version: str
) -> list[str]:
    """Build Previous Versions section from list of versions, excluding current."""
    lines = [
        "## Previous Versions",
        "",
        "To see documentation for previous versions of this driver, see the following:",
        "",
    ]

    for version in versions:
        if version != current_version:
            lines.append(f"- [{version}](./{version}.md)")

    # Add blank line after the list
    lines.append("")

    return lines


def update_previous_versions_section(
    content: str, all_versions: list[str], current_version: str
) -> str:
    """Replace Previous Versions section in content with filesystem-based list."""
    lines = content.split("\n")

    # Find Previous Versions section
    prev_versions_start = -1
    prev_versions_end = -1

    for i, line in enumerate(lines):
        if line.startswith("## Previous Versions"):
            prev_versions_start = i
            # Find the end (next ## heading or footnotes or end of file)
            for j in range(i + 1, len(lines)):
                if lines[j].startswith("##") or lines[j].startswith("[^"):
                    prev_versions_end = j
                    break
            if prev_versions_end == -1:
                # Section goes to end of file, but stop before footnotes
                for j in range(len(lines) - 1, i, -1):
                    if (
                        lines[j].strip()
                        and not lines[j].startswith("[^")
                        and not lines[j].startswith("[")
                    ):
                        prev_versions_end = j + 1
                        break
            break

    if prev_versions_start != -1:
        new_prev_section = build_previous_versions_section(
            all_versions, current_version
        )
        if prev_versions_end != -1:
            lines = (
                lines[:prev_versions_start]
                + new_prev_section
                + lines[prev_versions_end:]
            )
        else:
            lines = lines[:prev_versions_start] + new_prev_section

    return "\n".join(lines)


def replace_section(
    lines: list[str], start_marker: str, end_marker: str, new_content: list[str]
) -> list[str]:
    """Replace content between start_marker and end_marker with new_content.

    Returns the modified lines. If markers aren't found, returns original lines.
    """
    start_idx = -1
    end_idx = -1

    # Find start marker
    for i, line in enumerate(lines):
        if start_marker in line:
            start_idx = i
            break

    if start_idx == -1:
        return lines

    # Find end marker
    for i in range(start_idx + 1, len(lines)):
        if end_marker in line:
            end_idx = i
            break

    if end_idx == -1:
        return lines

    # Replace the section
    return lines[:start_idx] + new_content + lines[end_idx + 1 :]


def extract_title_from_content(content: str) -> Optional[str]:
    """Extract the title (# heading) from content, skipping frontmatter and anchors."""
    lines = content.split("\n")
    in_frontmatter = False
    frontmatter_closed = False

    for i, line in enumerate(lines):
        # Detect frontmatter start
        if i == 0 and line.strip() == "---":
            in_frontmatter = True
            continue

        # Detect frontmatter end
        if in_frontmatter and line.strip() == "---":
            in_frontmatter = False
            frontmatter_closed = True
            continue

        # Skip lines inside frontmatter
        if in_frontmatter:
            continue

        # Skip anchors
        if line.startswith("(") and line.endswith(")="):
            continue

        # Found a heading (must be after frontmatter is closed)
        if line.startswith("# ") and frontmatter_closed:
            return line

    return None


def strip_version_from_title(title: str, version: str) -> str:
    """Remove version suffix from title.

    Examples:
        '# MySQL/MariaDB Driver v0.5.0' -> '# MySQL/MariaDB'
        '# BigQuery Driver v1.2.0' -> '# BigQuery'
        '# Snowflake v3.0.0' -> '# Snowflake'
    """
    # Remove common patterns: "Driver v0.5.0", "v0.5.0", etc.
    patterns = [
        rf"\s+Driver\s+{re.escape(version)}$",  # " Driver v0.5.0"
        rf"\s+{re.escape(version)}$",  # " v0.5.0"
        r"\s+Driver$",  # " Driver" (if version was already removed)
    ]

    result = title
    for pattern in patterns:
        result = re.sub(pattern, "", result)

    return result


def update_index_header(
    content: str,
    driver: str,
    version: str,
    release_date: str,
    all_versions: list[str],
    existing_title: Optional[str] = None,
) -> str:
    """Update the index.md with new version info, regenerate TOC and Previous Versions from filesystem."""
    lines = content.split("\n")

    # Update copyright year
    for i, line in enumerate(lines):
        if line.startswith("# Copyright (c)"):
            year = datetime.now().year
            lines[i] = f"# Copyright (c) {year} ADBC Drivers Contributors"
            break

    # Find the title line and replace it with non-versioned title
    # Also remove the anchor line above it
    #
    # Turns:
    #
    # (driver-mysql-v0.5.0)=
    # MySQL/MariaDB Driver v0.5.0
    #
    # Into:
    #
    # MySQL/MariaDB
    #
    title_index = -1
    current_title = None
    in_frontmatter = False
    frontmatter_closed = False

    for i, line in enumerate(lines):
        # Track frontmatter boundaries
        if i == 0 and line.strip() == "---":
            in_frontmatter = True
            continue
        if in_frontmatter and line.strip() == "---":
            in_frontmatter = False
            frontmatter_closed = True
            continue

        # Find title (must be after frontmatter)
        if line.startswith("# ") and frontmatter_closed:
            title_index = i
            current_title = line
            # Check if previous line is a driver version anchor (e.g., (driver-mysql-v0.5.0)=)
            if i > 0 and re.match(
                r"^\(driver-[^-]+-v[\d.]+.*\)=$", lines[i - 1].strip()
            ):
                lines.pop(i - 1)
                title_index = i - 1
            break

    if title_index == -1:
        print("Warning: Could not find title line")
    else:
        # Determine the non-versioned title
        if existing_title:
            # Use the title from existing index.md
            title = existing_title
        else:
            # Strip version from the downloaded content's title
            title = strip_version_from_title(current_title, version)

        lines[title_index] = title

    # Replace or insert TOC section
    # Look for existing TOC between :::{toctree} and :::
    toc_start = -1
    toc_end = -1
    for i, line in enumerate(lines):
        if ":::{toctree}" in line:
            toc_start = i
        elif toc_start != -1 and line.strip() == ":::":
            toc_end = i
            break

    new_toc = build_toc_section(all_versions)

    if toc_start != -1 and toc_end != -1:
        # Replace existing TOC
        lines = lines[:toc_start] + new_toc + lines[toc_end + 1 :]
    else:
        # Insert TOC after title
        insert_pos = title_index + 1
        while insert_pos < len(lines) and not lines[insert_pos].strip():
            insert_pos += 1
        lines = lines[:insert_pos] + new_toc + lines[insert_pos:]

    # Update the badge line with new version and date
    for i, line in enumerate(lines):
        if line.startswith("[{badge-primary}`Driver Version|"):
            line = re.sub(r"Driver Version\|v[\d.]+", f"Driver Version|{version}", line)
            line = re.sub(r"#driver-[^-]+-v[\d.]+", f"#driver-{driver}-{version}", line)
            line = re.sub(r"Release Date\|[\d-]+", f"Release Date|{release_date}", line)
            lines[i] = line
            break

    # Replace Previous Versions section entirely with filesystem truth
    content_with_prev = update_previous_versions_section(
        "\n".join(lines), all_versions, version
    )
    return content_with_prev


def update_changelog(
    changelog_path: Path, version: str, release_date: str, release_body: str
) -> None:
    """Update the changelog.md file with new release notes."""
    if not changelog_path.exists():
        print(f"Warning: {changelog_path} does not exist, skipping changelog update")
        return

    content = changelog_path.read_text()
    lines = content.split("\n")

    # Check if this version already exists in the changelog
    version_header = f"## {version} ({release_date})"
    if version_header in content:
        print(f"Version {version} already exists in changelog, skipping update")
        return

    # Find where to insert the new changelog entry (after the "# Changelog" line)
    insert_index = -1
    for i, line in enumerate(lines):
        if line.startswith("# Changelog"):
            insert_index = i + 1
            # Skip empty lines
            while insert_index < len(lines) and not lines[insert_index].strip():
                insert_index += 1
            break

    if insert_index == -1:
        print("Warning: Could not find changelog header")
        return

    # Create new changelog entry
    new_entry = [
        "",
        f"## {version} ({release_date})",
        "",
        "<!-- NOTE: The items below have been automatically extracted from GitHub release body. Consider each item carefully and rewrite or improve any that aren't clear enough. Remove this comment before committing. -->",
        "",
        "",
    ]

    # Add release body (changelog content), but filter out "Detailed Changelog" section
    if release_body:
        release_lines = release_body.strip().split("\n")
        filtered_lines = []
        skip_section = False

        for line in release_lines:
            # Start skipping at "## Detailed Changelog"
            if line.strip().startswith("## Detailed Changelog"):
                skip_section = True
                continue

            # Stop skipping when we hit another ## heading
            if (
                skip_section
                and line.strip().startswith("##")
                and "Detailed Changelog" not in line
            ):
                skip_section = False

            # Include line if not in skip section
            if not skip_section:
                # Strip GitHub PR/issue references like " (#116)" or "(#116)"
                cleaned_line = re.sub(r"\s*\(#\d+\)", "", line)
                filtered_lines.append(cleaned_line)

        new_entry.extend(filtered_lines)
    else:
        new_entry.append("No changelog provided.")

    # Insert the new entry
    lines[insert_index:insert_index] = new_entry

    changelog_path.write_text("\n".join(lines))


def main():
    parser = argparse.ArgumentParser(
        description="Sync driver documentation from GitHub releases"
    )
    parser.add_argument("repo_name", help="Repository name (e.g., 'mysql')")
    parser.add_argument("release_tag", help="Release tag (e.g., 'go/v0.5.0')")
    parser.add_argument(
        "--repo-org",
        default="adbc-drivers",
        help="Repository organization (default: adbc-drivers)",
    )

    args = parser.parse_args()

    repo_org = args.repo_org
    repo_name = args.repo_name
    release_tag = args.release_tag
    version = extract_version_from_tag(release_tag)

    # Check if gh CLI is installed
    try:
        subprocess.run(
            ["gh", "--version"],
            capture_output=True,
            check=True,
        )
    except FileNotFoundError:
        print("Error: gh CLI is not installed or not in PATH")
        print("Please install it from: https://cli.github.com/")
        sys.exit(1)
    except subprocess.CalledProcessError:
        print("Error: gh CLI is installed but returned an error")
        sys.exit(1)

    print(f"Looking for release {release_tag} in {repo_org}/{repo_name}...")

    # Check if repo exists first
    if not check_repo_exists(repo_org, repo_name):
        print(f"Error: Repo '{repo_name}' not found in {repo_org} org")
        sys.exit(1)

    # Find the release (including drafts)
    release = find_release(repo_org, repo_name, release_tag)
    if not release:
        print(f"Error: Release {release_tag} not found in repo {repo_org}/{repo_name}")
        sys.exit(1)

    print(f"Found release: {release['name']} (draft: {release.get('draft', False)})")

    # Extract release date
    release_date = release["published_at"] or release["created_at"]
    if release_date:
        release_date = release_date.split("T")[0]  # Get YYYY-MM-DD
    else:
        release_date = datetime.now().strftime("%Y-%m-%d")

    # Find the .md asset
    md_asset = None
    for asset in release.get("assets", []):
        if asset["name"] == f"{repo_name}.md":
            md_asset = asset
            break

    if not md_asset:
        print(f"Error: {repo_name}.md asset not found in release")
        sys.exit(1)

    # Setup paths
    script_dir = Path(__file__).parent
    docs_root = script_dir.parent
    driver_dir = docs_root / "drivers" / repo_name

    if not driver_dir.exists():
        print(f"Error: Driver directory {driver_dir} does not exist")
        sys.exit(1)

    index_path = driver_dir / "index.md"
    version_path = driver_dir / f"{version}.md"
    changelog_path = driver_dir / "changelog.md"

    # Extract existing title from index.md if it exists
    existing_title = None
    if index_path.exists():
        existing_content = index_path.read_text()
        existing_title = extract_title_from_content(existing_content)
        if existing_title:
            print(f"Found existing title: {existing_title}")

    # Download the asset to a temporary location first
    temp_md = driver_dir / f".{repo_name}_temp.md"
    print(f"Downloading {md_asset['name']}...")
    download_asset(md_asset["url"], temp_md)

    # Read the downloaded content
    new_content = temp_md.read_text()

    # Copy to version-specific file first (so it appears in filesystem)
    print(f"Copying {repo_name}.md -> {version}.md...")
    version_path.write_text(new_content)

    # Now scan filesystem for ALL versions (including the one we just created)
    all_versions = get_all_versions_from_filesystem(driver_dir)
    print(
        f"Found {len(all_versions)} versions on filesystem: {', '.join(all_versions)}"
    )

    # Update Previous Versions section in the versioned file based on filesystem
    print(f"Updating Previous Versions in {version}.md...")
    versioned_content = update_previous_versions_section(
        new_content, all_versions, version
    )
    version_path.write_text(versioned_content)

    # Generate index.md from downloaded file (with title, TOC, and Previous Versions modifications)
    print(
        f"Generating index.md from {repo_name}.md (replacing title, TOC, and Previous Versions)..."
    )
    updated_content = update_index_header(
        new_content, repo_name, version, release_date, all_versions, existing_title
    )
    index_path.write_text(updated_content)

    # Update changelog
    print("Updating changelog.md...")
    release_body = release.get("body", "")
    update_changelog(changelog_path, version, release_date, release_body)

    # Clean up temp file
    temp_md.unlink()

    print(f"\n✅ Successfully synced {repo_name} documentation for {version}")
    print(f"   - Updated: {index_path}")
    print(f"   - Created: {version_path}")
    print(f"   - Updated: {changelog_path}")


if __name__ == "__main__":
    main()
