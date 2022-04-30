from urllib import response
from bs4 import BeautifulSoup
import requests
import urllib.request
from csv import reader
import pandas as pd
import logging


read_obj = open('tranco_QYW4.csv', 'r') 
csv_reader =  reader(read_obj)

logging.basicConfig(filename="logfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='a')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


for count, url in enumerate(csv_reader):
    new_url = url[0] 
    try:
        headers= {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}
        req = requests.get('http://' + new_url, data=None, headers=headers).text
        soup = BeautifulSoup(req, 'html.parser')
        server = soup.select('server')
        print(new_url, server)

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

    except urllib.error.HTTPError as e:
        print(new_url , e.headers.get('Server'))
    except urllib.error.URLError as e:
        print(new_url, 'FAILED:', e.reason)
        logger.info("Url Error - Website URL: %s Reason: %s",new_url, e.reason)
    except ConnectionResetError as e:
        continue

    if count == 99:
        break
        
#printing the title of the given website 



