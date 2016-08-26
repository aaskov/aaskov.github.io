# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
from os import listdir
from os.path import isfile, join


my_path = '/var/www/html/github/content'
page_location = 'pages/'
content_location = 'content/'
archive_path = '/var/www/html/github/archive.html'

# Get the list of content files
onlyfiles = [f for f in listdir(my_path) if isfile(join(my_path, f))]

# Get content
with open(content_location+onlyfiles[1], 'r') as f:
    _raw = f.read()

# Run exec
exec _raw

# Construct pages
header = """<!DOCTYPE html><html><head><title>aaskov</title><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><meta http-equiv="Content-language" content="en"><link rel="stylesheet" href="../stylesheet.css" type="text/css" /></head><body><div id="page"><div id="top"><p class="logo"><a href="../index.php">Aaskov, Rasmus</a></p></div>"""

# Content
html = """<div id="content">"""
html += """<h3>"""+meta['title']+"""</h3>"""
html += """<p class="date">"""+meta['date']+"""</p>"""
html += content
html += """</br>"""
html += """</div>"""

# Footer
footer = """</div></body></html>"""

# Write to file
with open(page_location+meta['title'].replace(' ', '_')+'.php', 'w') as f:
    f.write(str(header+html+footer))

# Update archive

