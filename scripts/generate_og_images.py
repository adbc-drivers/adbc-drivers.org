#!/usr/bin/env python3
"""Generate Open Graph images for Jekyll blog posts.

Reads post front matter (title, date) and renders a branded 1200x630 PNG
for each post. Fonts are converted from the site's woff2 files at runtime.
"""

import os
import re
import tempfile
from pathlib import Path

import yaml
from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont

WIDTH = 1200
HEIGHT = 630
BG = "#000000"
WHITE = "#ffffff"
GRAY = "#999999"
PADDING_X = 80


def convert_woff2_to_ttf(woff2_path, output_dir):
    """Convert a woff2 font to ttf so Pillow can use it."""
    ttf_path = os.path.join(output_dir, Path(woff2_path).stem + ".ttf")
    font = TTFont(woff2_path)
    font.flavor = None
    font.save(ttf_path)
    return ttf_path


def parse_front_matter(filepath):
    """Extract YAML front matter from a Jekyll post."""
    with open(filepath) as f:
        content = f.read()
    m = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not m:
        return None
    return yaml.safe_load(m.group(1))


def date_from_filename(filename):
    """Format a human-readable date from a Jekyll post filename."""
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})", filename)
    if not m:
        return ""
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December",
    ]
    return f"{months[int(m.group(2)) - 1]} {int(m.group(3))}, {m.group(1)}"


def wrap_text(draw, text, font, max_width):
    """Word-wrap text to fit within max_width pixels."""
    words = text.split()
    lines, current = [], ""
    for word in words:
        test = f"{current} {word}".strip()
        if draw.textbbox((0, 0), test, font=font)[2] <= max_width:
            current = test
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def generate_image(title, date_str, output_path, fonts, logo):
    """Render a single OG image."""
    img = Image.new("RGB", (WIDTH, HEIGHT), BG)
    draw = ImageDraw.Draw(img)
    max_text_width = WIDTH - PADDING_X * 2

    # Accent bar across the top
    draw.rectangle([(0, 0), (WIDTH, 4)], fill=WHITE)

    # Logo in the upper right
    logo_margin = 36
    img.paste(logo, (WIDTH - logo.width - logo_margin, logo_margin))

    # Pick font size — shrink if the title needs more than 3 lines
    title_font = fonts["bold_lg"]
    lines = wrap_text(draw, title, title_font, max_text_width)
    if len(lines) > 3:
        title_font = fonts["bold_sm"]
        lines = wrap_text(draw, title, title_font, max_text_width)

    line_height = int(draw.textbbox((0, 0), "Ag", font=title_font)[3] * 1.05)

    # Build from the bottom: title block flush to bottom with padding
    bottom_pad = 64
    title_y = HEIGHT - bottom_pad - line_height * len(lines[:4])

    # Date above the title
    date_bbox = draw.textbbox((0, 0), date_str, font=fonts["date"])
    date_height = date_bbox[3] - date_bbox[1]
    draw.text((PADDING_X, title_y - date_height - 20), date_str, font=fonts["date"], fill=GRAY)

    for line in lines[:4]:
        draw.text((PADDING_X, title_y), line, font=title_font, fill=WHITE)
        title_y += line_height

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path, "PNG", optimize=True)
    print(f"  \u2192 {output_path}")


def load_fonts(font_dir):
    """Convert woff2 fonts to ttf and load them for Pillow."""
    tmpdir = tempfile.mkdtemp()
    ttf = {}
    for name in ("Inter-Bold", "Inter-Regular"):
        woff2 = os.path.join(font_dir, f"{name}.woff2")
        if os.path.exists(woff2):
            ttf[name] = convert_woff2_to_ttf(woff2, tmpdir)
        else:
            print(f"Warning: {woff2} not found")
            ttf[name] = None

    def _load(key, size):
        if ttf.get(key):
            return ImageFont.truetype(ttf[key], size)
        return ImageFont.load_default(size)

    return {
        "bold_lg": _load("Inter-Bold", 52),
        "bold_sm": _load("Inter-Bold", 42),
        "regular": _load("Inter-Regular", 24),
        "date": _load("Inter-Regular", 32),
    }


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Generate OG images for blog posts")
    parser.add_argument("--posts-dir", default="_posts")
    parser.add_argument("--output-dir", default="assets/images/og")
    parser.add_argument("--font-dir", default="assets/fonts")
    args = parser.parse_args()

    fonts = load_fonts(args.font_dir)

    # Load and scale the logo for the upper-right corner
    logo_path = os.path.join("assets", "images", "adbc-drivers-logo.png")
    logo_full = Image.open(logo_path)
    logo_height = 220
    logo_width = int(logo_full.width * logo_height / logo_full.height)
    logo = logo_full.resize((logo_width, logo_height), Image.LANCZOS)

    posts_dir = Path(args.posts_dir)
    for post_file in sorted(posts_dir.glob("*.md")):
        fm = parse_front_matter(post_file)
        if not fm:
            continue
        title = fm.get("title", "Untitled")
        date_str = date_from_filename(post_file.name)
        output = os.path.join(args.output_dir, f"{post_file.stem}.png")
        print(f"Generating: {title}")
        generate_image(title, date_str, output, fonts, logo)


if __name__ == "__main__":
    main()
