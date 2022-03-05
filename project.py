from urllib import response
from bs4 import BeautifulSoup
import requests
import urllib.request
from csv import reader
import pandas as pd

"""
#try 1 - BV - not really sure about this one..need to do more research
url =  'http://www.bethanyvella.com/'
response = requests.get(url)

#printing the title of the given website
soup =  BeautifulSoup(response.text, 'html.parser')
print(soup.title)
print(soup)

"""

#try2 - RA
"""
filename ='tranco_QYW4.csv'
df = pd.read_csv(filename)
print(df)

for count, url in df.iterrows():
    response = urllib.request.urlopen(url)
    print(url)
    if count == 99:
        break 


"""
read_obj = open('tranco_QYW4.csv', 'r') 
csv_reader =  reader(read_obj)
#csv_reader = ['google.com', 'youtube.com', 'facebook.com']
for count, url in enumerate(csv_reader):
    new_url = url[0] 
    try:
        response = urllib.request.urlopen('https://'+new_url)
        print(new_url , response.info().get('Server'))
    except urllib.error.HTTPError as e:
        print(new_url , e.headers.get('Server'))
    except urllib.error.URLError as e:
        print(new_url, 'FAILED:', e.reason)
    
    if count == 99:
        break
        

#url =  'http://www.bethanyvella.com/'
"""
response = urllib.request.urlopen(url)
print(response.code)
print(response.headers)

info = response.info()
print(response.info().get('Server'))
print(url)
response_content = response.read()
#print(response_content)

"""


