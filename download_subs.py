#!/usr/bin/python

import requests
import urllib.request
import time
from bs4 import BeautifulSoup

import struct, os

def hashFile(name):
    try:
        longlongformat = '<q'  # little-endian long long
        bytesize = struct.calcsize(longlongformat)

        f = open(name, "rb")

        filesize = os.path.getsize(name)
        print(filesize)
        hash = filesize

        if filesize < 65536 * 2:
            return "SizeError"

        for x in range(65536//bytesize):
            buffer = f.read(bytesize)
            (l_value,)= struct.unpack(longlongformat, buffer)
            hash += l_value
            hash = hash & 0xFFFFFFFFFFFFFFFF #to remain as 64bit number

            f.seek(max(0,filesize-65536),0)
            for x in range(65536//bytesize):
                buffer = f.read(bytesize)
                (l_value,)= struct.unpack(longlongformat, buffer)
                hash += l_value
                hash = hash & 0xFFFFFFFFFFFFFFFF

            f.close()
            returnedhash =  "%016x" % hash
            return returnedhash

    except(IOError):
        return "IOError"

url = 'https://www.aftonbladet.se/'
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

#for i in range(36,len(soup.findAll('a'))):
#    one_a_tag = soup.findAll('a')[i]
#    link = one_a_tag['href']
#    print("https://www.aftonbladet.se%s" % (link))


print(hashFile("/home/daniel/Downloads/Game.of.Thrones.Season.2.720p.BluRay.x264.ShAaNiG/Game.of.Thrones.S02E10.720p.BluRay.500MB.ShAaNiG.com.mkv"))
print(hashFile("/home/daniel/Downloads/breakdance.avi"))
