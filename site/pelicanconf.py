#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'CodeCachet'
SITENAME = """<span style="font-family: 'Righteous', cursive;color:red">Code<span style="color:black">Cachet</span></span>"""
#SITEURL = 'https://codecachet.org'
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

THEME = 'mythemes/elegant'

PLUGIN_PATHS = ['plugins']   # Name of the directory where plugin are kept.
#PLUGINS = ['sitemap']       # Name of the particular plugin inside the directory.

PLUGINS = ['sitemap', 'tipue_search', 'extract_toc', 'neighbors']

# to generate favicon
STATIC_PATHS = ['theme/images', 'images']
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
LANDING_PAGE_ABOUT = {
    'title' : 'This Amazing Journey',
    'details': '<p>it begins</p> <p>with the first step</p>'
}

#PROJECTS = [
#    {
#        'name' : 'Coding Python for the Web',
#        'url' : 'https://codecachet.org',
#        'description' : 'Learn all about this thing called Python'
#    }
#]
