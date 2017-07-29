import requests
from bs4 import BeautifulSoup
import operator


def start(url):
    wordlist = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code)
    for post_text in soup.findAll('a',{'class':'imagecache'}):
        content = post_text.string
        words = content.lower().split()
        for word in words:
            wordlist.append(word)


start('https://www.kemkominfo.go.id')


