from urllib import response
from bs4 import BeautifulSoup
import requests
import urllib.request
from csv import reader
import pandas as pd
import logging

"""
#try 1 - BV - not really sure about this one..need to do more research
url =  'http://www.bethanyvella.com/'
response = requests.get(url)

#printing the title of the given website
soup =  BeautifulSoup(response.text, 'html.parser')
print(soup.title)
print(soup)
scripts = soup.select('script')
for s in scripts:
    print(s)


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
logging.basicConfig(filename="logfile2.log",
                    format='%(asctime)s %(message)s',
                    filemode='a')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
 
for count, url in enumerate(csv_reader):
    new_url = url[0] 
    try:
        
        req = urllib.request.Request(
            'http://'+new_url,
            data=None,
            headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}
        )
        response = urllib.request.urlopen(req)
        
        print(new_url , response.info().get('Server'))
        
    except urllib.error.HTTPError as e:
        print(new_url , e.headers.get('Server'))
    except urllib.error.URLError as e:
        print(new_url, 'FAILED:', e.reason)
        logger.info("Url Error - Website URL: %s Reason: %s",new_url, e.reason)
    except ConnectionResetError as e:
        continue
    
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


