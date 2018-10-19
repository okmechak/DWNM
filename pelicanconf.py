#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
import os.path


AUTHOR = 'Oleg Kmechak'
SITENAME = 'Oleg Kmechak'
SITEURL = ''

# all defaults to True.
DISPLAY_HEADER = True
DISPLAY_FOOTER = True
DISPLAY_HOME   = True
DISPLAY_MENU   = True


TAGS_URL           = 'tags'
TAGS_SAVE_AS       = 'tags/index.html'
AUTHORS_URL        = 'authors'
AUTHORS_SAVE_AS    = 'authors/index.html'
CATEGORIES_URL     = 'categories'
CATEGORIES_SAVE_AS = 'categories/index.html'
ARCHIVES_URL       = 'archives'
ARCHIVES_SAVE_AS   = 'archives/index.html'
EN_URL             = 'index.html'
EN_SAVE_AS         = 'index.html'
UA_URL             = 'ua/index.html'
UA_SAVE_AS         = 'ua/index.html'
ABOUT_URL          = 'category/about'
ABOUT_SAVE_AS      = 'category/about.html'



MENU_INTERNAL_PAGES = (
    #('Authors', AUTHORS_URL, AUTHORS_SAVE_AS),
    ('Categories', CATEGORIES_URL, CATEGORIES_SAVE_AS),
    ('Archives', ARCHIVES_URL, ARCHIVES_SAVE_AS),
    ('About', ABOUT_URL, ABOUT_SAVE_AS),
    #('En', EN_URL, EN_SAVE_AS),#TODO
    #('Укр', UA_URL, UA_SAVE_AS),#TODO!!
    ('Tags', TAGS_URL, TAGS_SAVE_AS)
)

PELICAN_DIR = ''
if "PELICAN" in os.environ:
    PELICAN_DIR = os.environ["PELICAN"]
else: 
    print("SOMETHING WRONG!")
    print(os.environ)



THEME = os.path.join(PELICAN_DIR, 'blue-penguin') #medius, waterspill, blue-penguin
print(THEME)
PATH = 'content'

TIMEZONE = 'Europe/Kiev'

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
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True



PLUGIN_PATHS = [os.path.join(PELICAN_DIR, 'pelican-plugins')]
print(PLUGIN_PATHS)
PLUGINS = ['render_math', 'assets']#'i18n_subsites' FIXME

#multilanguage setup
DEFAULT_LANG = 'en'

STATIC_PATHS = ['Images', 'Images/hello_world', 'Images/icons', 'Files']
IGNORE_FILES = ['.DS_Store', 'pneumatic.scss', 'pygments.css']

DISPLAY_PAGES_ON_MENU = True

SUMMARY_MAX_LENGTH = 40

CACHE_CONTENT = False
DELETE_OUTPUT_DIRECTORY = True