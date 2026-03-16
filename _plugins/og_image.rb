# Automatically set the OG image for blog posts.
#
# If an OG image has been generated at assets/images/og/<slug>.png,
# use it instead of the site-wide default.  Posts can still override
# by setting `image:` explicitly in their front matter.

Jekyll::Hooks.register :posts, :pre_render do |post|
  site_default = post.site.config.dig("defaults", 0, "values", "image")
  has_custom_image = post.data["image"] && post.data["image"] != site_default

  unless has_custom_image
    slug = File.basename(post.path, File.extname(post.path))
    og_file = File.join(post.site.source, "assets", "images", "og", "#{slug}.png")
    if File.exist?(og_file)
      post.data["image"] = "/assets/images/og/#{slug}.png"
    end
  end
end
