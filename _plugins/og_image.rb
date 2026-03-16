# Automatically generate and set OG images for blog posts.
#
# On site init, runs the Python script to generate OG images.
# Then, for each post, sets the OG image path if the file exists.
# Posts can still override by setting `image:` explicitly in front matter.

Jekyll::Hooks.register :site, :after_init do |site|
  script = File.join(site.source, "scripts", "generate_og_images.py")
  if File.exist?(script)
    Jekyll.logger.info "OG Images:", "Generating..."
    system("python3", script) or Jekyll.logger.warn("OG Images:", "Generation failed")
  end
end

Jekyll::Hooks.register :posts, :pre_render do |post|
  slug = File.basename(post.path, File.extname(post.path))
  og_file = File.join(post.site.source, "assets", "images", "og", "#{slug}.png")
  if File.exist?(og_file)
    post.data["image"] = "/assets/images/og/#{slug}.png"
  end
end
