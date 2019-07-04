#!/usr/bin/python

import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = 'https://www.aftonbladet.se/'
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

for i in range(36,len(soup.findAll('a'))):
    one_a_tag = soup.findAll('a')[i]
    link = one_a_tag['href']
    print("https://www.aftonbladet.se%s" % (link))
