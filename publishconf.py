#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'datayear.us'
RELATIVE_URLS = True
DISQUS_SITENAME = 'datayear'
GOOGLE_ANALYTICS = 'UA-34603374-3'

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""


THEME = "pelican-bootstrap3"

# Social widget
SOCIAL = (('github', 'https://github.com/brianlawrence2/datayear/'),
          ('twitter', 'https://twitter.com/importantbrian'),)
