#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'CodeCachet'
SITENAME = """<span style="font-family: 'Righteous', cursive;color:red">Code<span style="color:black">Cachet</span></span>"""
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL_PROFILE_LABEL = 'Visit Us!'

SOCIAL = (('Twitter', 'https://twitter.com/CodeCachet'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'themes/elegant'

#PLUGIN_PATHS = ['plugins']   # Name of the directory where plugin are kept.
#PLUGINS = ['sitemap']       # Name of the particular plugin inside the directory.

PLUGINS = ['sitemap', 'extract_toc', 'neighbors', 'books', 'prettify']
#PLUGINS = ['sitemap', 'neighbors', 'books']

# to generate favicon
STATIC_PATHS = ['theme/images', 'images', 'pdfs', 'static/css']
USE_SHORTCUT_ICONS = True


MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc' :{'permalink' : 'true'},

    },
    'output_format': 'html5',
}

# for elegant
# NOTE: text is now in pages/about_site.md

LANDING_PAGE_ABOUT = {
   'snippet' : 'about_us'
}

#PROJECTS = [
#    {
#        'name' : 'Coding Python for the Web',
#        'url' : 'https://codecachet.org',
#        'description' : 'Learn all about this thing called Python'
#    }
#]
DISPLAY_CATEGORIES_MENU_BUTTON = True
# DISPLAY_SEARCH_BAR = True
DISPLAY_GOOGLE_SEARCH_BAR = True
GOOGLE_SEARCH_BAR_ID = '007630758047090875401:rfhru89uxou'

DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'archives']
THEME_TEMPLATES_OVERRIDES = ['my_templates']
MENU_PAGE_ORDER_USE = True
MENU_PAGE_ORDER = ['Books', 'Resources', 'Contact']

PAGE_PATHS = ['pages']
ARTICLE_EXCLUDES = ['books']
BOOKS_PAGES_HOME = 'books'

# NOTE: books.py plugin is in my_plugins
PLUGIN_PATHS = ['plugins', 'my_plugins']

# dg - mod to temporarily fix bug in extract_toc.py plugin which sometimes thinks there is a toc via [TOC],
#   when it is an empty <ul> list, so still would display an empty "Contents". Not sure why!!!
SHOW_TOC = True

# DISQUS_SITENAME = 'codecachet'
PRETTIFY_WITH_BS4 = False # us bs4 to prettify output
