source "https://rubygems.org"

gem "github-pages", group: :jekyll_plugins
gem "webrick", "~> 1.8"

# Ruby 3.4 dropped csv/base64/bigdecimal/logger from default gems; jekyll
# 3.9.x (pinned by github-pages) still requires them. Pin them here so
# `bundle install` resolves them as regular gems.
gem "csv"
gem "base64"
gem "bigdecimal"
gem "logger"

group :jekyll_plugins do
  gem "jekyll-relative-links"
end
