#! /usr/bin/env python

import requests
from bs4 import BeautifulSoup
import sys

def page_listings(url):
  r = []
  c = requests.get(url).text
  soup = BeautifulSoup(c, 'html.parser')
  for l in soup.find_all(class_="site-listing"):
    r.append(l.find("a").text)
  return r

def top_n(n):
  r = []
  i = 0
  while len(r) < n:
    r.extend(page_listings("http://www.alexa.com/topsites/global;" + str(i)))
    i += 1
  return r[:n]

for l in top_n(int(sys.argv[1])):
  print l

