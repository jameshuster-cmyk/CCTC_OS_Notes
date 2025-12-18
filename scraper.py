#!/usr/bin/python
import lxml.html
import requests

page = requests.get('http://192.168.28.111/sites/index.html')
tree = lxml.html.fromstring(page.content)

authors = tree.xpath('//dd[@class="org-title"]/text()')

print ('Authors: ',authors)
