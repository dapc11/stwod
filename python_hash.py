import struct, os, sys, requests
from bs4 import BeautifulSoup


def hashFile(name):
    try:
        longlongformat = '<q'  # little-endian long long
        bytesize = struct.calcsize(longlongformat)

        f = open(name, "rb")

        filesize = os.path.getsize(name)
        hash = filesize

        if filesize < 65536 * 2:
            return "SizeError"

        for x in range(65536 / bytesize):
            buffer = f.read(bytesize)
            (l_value, ) = struct.unpack(longlongformat, buffer)
            hash += l_value
            hash = hash & 0xFFFFFFFFFFFFFFFF  #to remain as 64bit number

        f.seek(max(0, filesize - 65536), 0)
        for x in range(65536 / bytesize):
            buffer = f.read(bytesize)
            (l_value, ) = struct.unpack(longlongformat, buffer)
            hash += l_value
            hash = hash & 0xFFFFFFFFFFFFFFFF

        f.close()
        returnedhash = "%016x" % hash
        return returnedhash

    except (IOError):
        return "IOError"


def get_href(url='https://www.opensubtitles.com', part_of_link=''):
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, features='html5lib')
    for l in soup.find_all('a'):
        href = l.get('href')
        if href is not None and part_of_link in href:
            return href


hash = hashFile(sys.argv[1])

link = get_href("https://www.opensubtitles.com/sv/search/moviehash/" + hash,
                '/sv/subtitles/')

link = get_href('https://www.opensubtitles.com' + link,
                'https://www.opensubtitles.com/se/subtitles/')

link = get_href(link, '/buttons')
link = get_href('https://www.opensubtitles.com' + link, 'nocache')
print('https://www.opensubtitles.com' + link)
