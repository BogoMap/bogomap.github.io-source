#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

### PELICAN Properties
# http://docs.getpelican.com/en/3.6.3/settings.html

## Basic settings

# PELICAN - Default author
AUTHOR = u'Equipo BogoMap'
# PELICAN - Your site name
SITENAME = u'BogoMap.co - Mapa del sistema de transporte de Bogota'
# PELICAN - The default date format you want to use.
DEFAULT_DATE_FORMAT = ('%d %B %Y')
# PELICAN - Base URL of your website.
#SITEURL = 'http://localhost:8000'
SITEURL = 'http://localhost'
#SITEURL = 'http://rutas.bogomap.co'
# PELICAN - Path to content directory to be processed by Pelican.
PATH = 'content'
# PELICAN - The timezone used in the date information, to generate Atom and RSS feeds
TIMEZONE = 'America/Bogota'
# Uncomment following line if you want document-relative URLs when developing
# PELICAN - Defines whether Pelican should use document-relative URLs or not.
#RELATIVE_URLS = True
# PELICAN - List of templates that are used directly to render content.
#DIRECT_TEMPLATES = ('index')
# PELICAN - A list of directories (relative to PATH) in which to look for static files.
STATIC_PATHS = ['images','php']
# Whether to display pages on the menu of the template.
# DISPLAY_PAGES_ON_MENU = true

# URL settings

# PELICAN - The location to save the article archives page.
ARCHIVES_SAVE_AS = False
# PELICAN - The location to save an author.
#AUTHOR_SAVE_AS = False
# PELICAN - The location to save a category.
#CATEGORY_SAVE_AS = False
# PELICAN - The URL we will use to link to a page.
PAGE_URL = '{slug}/'
# PELICAN - The location we will save the page.
PAGE_SAVE_AS = '{slug}/index.html'
# PELICAN - The location to save the tag page.
TAG_SAVE_AS = False

## Feed settings

# Feed generation is usually not desired when developing
# PELICAN - Relative URL to output the all-posts Atom feed
FEED_ALL_ATOM = None
# PELICAN - Relative URL to output the all-posts RSS feed
FEED_ALL_RSS = None
# PELICAN - Where to put the category Atom feeds.
CATEGORY_FEED_ATOM = None
# PELICAN - Where to put the author Atom feeds.
AUTHOR_FEED_ATOM = None
# PELICAN - Where to put the author Atom feeds.
AUTHOR_FEED_RSS = None

## Paginations

# PELICAN - The maximum number of articles to include on a page, not including orphans.
DEFAULT_PAGINATION = False

## Translations

# PELICAN - The default language to use.
DEFAULT_LANG = u'es'
# PELICAN - Where to put the Atom feed for translations.
TRANSLATION_FEED_ATOM = None

## Themes

# PELICAN - Theme to use to produce the output.
THEME = 'themes/mombacho'
# PELICAN - A subtitle to appear in the header.
SITESUBTITLE = 'Rutas y paraderos del SITP y Transmilenio'
# PELICAN - A list of tuples (Title, URL) for additional menu items to appear at the beginning of the main menu.
 #MENUITEMS = (('BogoMap', 'http://bogomap.co', 'map'),
 #             ('Rutas BogoMap', '/index.html', 'public-transport'),
 #             )
# PELICAN - A list of tuples (Title, URL) to appear in the “social” section.
SOCIAL = (('envelope-o', 'mailto:contacto@bogomap.co'),
          ('facebook', 'http://www.facebook.com/BogoMap'),
          ('twitter', 'http://www.twitter.com/BogoMap'),
          )
# Blogroll
# PELICAN - A list of tuples (Title, URL) for links to appear on the header.
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('You can modify those links in your config file', '#'),)


### FLEX theme properties
# https://github.com/alexandrevicenzi/Flex/wiki

# FLEX - Profile picture to show above author name (absolute url).
SITELOGO = '/images/bogomap-rutas.png'
# FLEX - Site description to use in meta tags.
SITEDESCRIPTION = 'Mapa de rutas y paraderos que conforman el sistema de transporte de Bogota'
# FLEX - language_TERRITORY for Open Graph.
OG_LOCALE = u'es_CO'
# FLEX - Creative Commons License to show on footer.
CC_LICENSE = { 'name': 'Creative Commons Attribution-ShareAlike', 'version':'4.0', 'slug': 'by-sa' }
# FLEX - Robots meta tag value.
ROBOTS = 'index, follow'
# FLEX - 
FAVICON = '/images/favicon.ico'
# FLEX -
USE_LESS = True

