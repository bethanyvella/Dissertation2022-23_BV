from ast import Compare
import imp
from msilib.schema import File
from urllib import response
from bs4 import BeautifulSoup
import requests
import urllib.request
from csv import reader
import pandas as pd
import logging
import os
import urllib3
from urllib3.exceptions import NewConnectionError
import hashlib


read_obj = open('robert.csv', 'r') 
csv_reader =  reader(read_obj)

logging.basicConfig(filename="logfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='a')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

parent_dir = "C:\\Users\\betha\\Desktop\\ITProject\\WebScrapingProject\\"
directory = "websites2\\"
col1 = "JS Path"
col2 = "Hash"
path1 = os.path.join(parent_dir, directory)
os.mkdir(path1)

for count, url in enumerate(csv_reader):
    new_url = url[0]
    try:
        path2 = os.path.join(parent_dir, directory, new_url)
        os.mkdir(path2)
    
        headers= {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}
        req = requests.get('http://' + new_url, data=None, headers=headers).text
        soup = BeautifulSoup(req, 'html.parser')
        server = soup.select('server')
        #print(new_url, server)

        scripts = soup.select('script')
        filenumber = 0
        for s in scripts:
            
            #filename = "%s.txt" % scripts
            if s.has_attr('src'):
                if s['src'].startswith("httyp"):
                    js = requests.get(s['src'])
                    #print(js)
                else:
                    if s['src'][0] != "/":
                        js = requests.get("http://"+new_url+"/"+s['src'])
                    else:
                        js = requests.get("http://"+new_url+s['src'])
                   
                jsPath = path2 + "\\" + s['src'].replace(':', '_').replace('/', '_').replace('?', '_')
                file = open(jsPath, "w", encoding='utf-8')
                file.write(js.text)
                file.close()
                with open(jsPath, 'rb') as jsScript:
                    file_buffer = jsScript.read()
                    result = hashlib.sha256(file_buffer)
                    #print(result.hexdigest())
                    data = pd.read_excel(r"jQuriesHashes.xlsx")
                    df = pd.DataFrame(data, columns=['Hash', 'Vulnrable'])
                    for index, row in df.iterrows():
                        #print(index, row['Hash'])
                        if row['Hash'] == result.hexdigest():
                            if row['Vulnrable'] == "Yes":
                                print("Vulnrable Library Ditected from" + new_url + jsPath)
                    
            else:
                filenumber +=1
                jsPath = path2 + "\\" + str(filenumber)
                file = open(jsPath, "w", encoding="utf-8")
                file.write(s.text)
                file.close()
                with open(jsPath, 'rb') as jsScript:
                    file_buffer = jsScript.read()
                    result = hashlib.sha256(file_buffer)
                    #print(result.hexdigest())
                    data = pd.read_excel(r"jQuriesHashes.xlsx")
                    df = pd.DataFrame(data, columns=['Hash','Vulnrable'])
                    for index, row in df.iterrows():
                        #print(index, row['Hash'])
                        if row['Hash'] == result.hexdigest():
                            if row['Vulnrable'] == "Yes":
                                print("Vulnrable Library Ditected from " + new_url + " "+ jsPath)

    except Exception as e:
        #print('Something unexpected happened', str(e))
        continue
    except urllib.error.HTTPError as e:
        print(new_url , e.headers.get('Server'))
    except urllib.error.URLError as e:
        #print(new_url, 'FAILED:', e.reason)
        logger.info("Url Error - Website URL: %s Reason: %s",new_url, e.reason)
    except ConnectionError as e:
        continue
    except ConnectionResetError as e:
        continue
    except TimeoutError as e:
        continue
    except urllib3.exceptions.TimeoutError as e:
        continue
    except NewConnectionError as e:
        continue
    except requests.exceptions.ConnectionError as e:
        continue
    
    if count == 999:
        break
        
#printing the title of the given website 



