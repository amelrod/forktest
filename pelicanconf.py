#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# Basics
AUTHOR = "Adam Melrod"
SITENAME = "Test"
SITEURL = ""

PATH = "content"
THEME = "theme"

TIMEZONE = "America/New_York"
DEFAULT_LANG = "en"
DEFAULT_DATE_FORMAT = "%B %-d, %Y"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Plugins and other functionality
PLUGINS = [
    "render_math",
    "pelican_webassets",
    "sitemap",
    "minchin.pelican.plugins.summary",
]
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.smarty": {},
    },
    "output_format": "html5",
}

# Path inputs
STATIC_PATHS = ["extra", "images", "js"]
EXTRA_PATH_METADATA = {
    f"extra/{filename}": {"path": filename}
    for filename in ["CNAME", ".nojekyll", "robots.txt"]
}

# Path and URL outputs
ARTICLE_URL = "{slug}"
ARTICLE_SAVE_AS = "{slug}.html"

PAGE_URL = "{slug}"
PAGE_SAVE_AS = "{slug}.html"
TAG_URL = "tag/{slug}"
TAG_SAVE_AS = "tag/{slug}.html"

AUTHOR_SAVE_AS = ""
CATEGORY_SAVE_AS = ""
AUTHORS_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""

# Pagination
DEFAULT_PAGINATION = 10
PAGINATION_PATTERNS = (
    (1, "{base_name}/", "{base_name}/index.html"),
    (2, "{base_name}/page/{number}", "{base_name}/page/{number}/index.html"),
)

# Other
FOOTER_LINKS = {
    "email": "mailto:abmelrod@umd.edu",
    "github": "https://github.com/amelrod",
}
FILENAME_METADATA = r"(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)"
SUMMARY_END_MARKER = "<!-- more -->"
