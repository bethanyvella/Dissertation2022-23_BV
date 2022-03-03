from urllib import response
from bs4 import BeautifulSoup
import requests
import urllib.request

#try 1 - BV - not really sure about this one..need to do more research
url =  'http://www.bethanyvella.com/'
response = requests.get(url)

#printing the title of the given website
soup =  BeautifulSoup(response.text, 'html.parser')
print(soup.title)
print(soup)

#try2 - RA
url =  'http://www.bethanyvella.com/'
response = urllib.request.urlopen(url)
print(response.code)
print(response.headers)

info = response.info()
print(response.info().get('Server'))
print(url)
response_content = response.read()
#print(response_content)

