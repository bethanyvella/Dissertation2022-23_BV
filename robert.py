from urllib import response
from bs4 import BeautifulSoup
import requests
import urllib.request
from csv import reader
import pandas as pd
import logging


#try 1 - BV - not really sure about this one..need to do more research
url =  'https://arkafort.robertabela.com/hotjar/'
response = requests.get(url)

#printing the title of the given website
soup =  BeautifulSoup(response.text, 'html.parser')
scripts = soup.select('script')
for s in scripts:
    if s.has_attr('src'):
        if s['src'].startswith("http"):
            js = requests.get(s['src'])
        else:
            js = requests.get(url+s['src'])
        print(js.text)
        print('---------------------------\n\n\n')

    else:
        print(s.text)

