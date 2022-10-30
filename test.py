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


read_obj = open('tranco_QYW4.csv', 'r') 
csv_reader =  reader(read_obj)
WINDOWS_LINE_ENDINGS = b'\r\n'
UNIX_LINE_ENDINGS = b'\n'

logging.basicConfig(filename="logfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='a')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

parent_dir = "C:\\Users\\betha\\Desktop\\ITProject-Dissertation\\WebScrapingProject\\"
directory = "websites\\"
col1 = "JS Path"
col2 = "Hash"
path1 = os.path.join(parent_dir, directory)
os.mkdir(path1)

vulnerabilityReportPath = os.path.join(parent_dir, "VulnerabilityReport.txt")
file = open(vulnerabilityReportPath, "w", encoding='utf-8')
file.write("--Vulnerability Report--")
file.close()

for count, url in enumerate(csv_reader):
    new_url = url[0]
    if(count == 1000):
        break
    
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
                if s['src'].startswith("http"):
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
                    #when the file is saved, Windows line endings are used (CRLF). When hashing these are changed to LF since the hash would change due to line endings
                    file_buffer = file_buffer.replace(WINDOWS_LINE_ENDINGS, UNIX_LINE_ENDINGS)

                    #opening the excel
                    data = pd.read_excel(r"JQueryHashes.xlsx")
                    df = pd.DataFrame(data, columns=['Hash', 'Vulnerable'])

                    #looping through
                    for index, row in df.iterrows():

                        #first checking with file name match
                        if s['src'] == row['URL']():
                            if row['Vulnerable'] == "Yes":
                                print("Vulnerable Library Detected from " + new_url + jsPath)
                                file = open(vulnerabilityReportPath, "a", encoding='utf-8')
                                file.write("\n--"+new_url+" | "+jsPath)
                                file.close()
                        else:
                            #if it doesnt match, try with hash
                            result = hashlib.sha256(file_buffer)
                            #print(result.hexdigest())
                    
                            for index, row in df.iterrows():
                            #print(index, row['Hash'])
                                if row['Hash'] == result.hexdigest():
                                    if row['Vulnerable'] == "Yes":
                                        print("Vulnerable Library Detected from " + new_url + jsPath)
                                        file = open(vulnerabilityReportPath, "a", encoding='utf-8')
                                        file.write("\n--"+new_url+" | "+jsPath)
                                        file.close()
                    
            else:
                filenumber +=1
                jsPath = path2 + "\\" + str(filenumber)
                file = open(jsPath, "w", encoding="utf-8")
                file.write(s.text)
                file.close()
                with open(jsPath, 'rb') as jsScript:
                    file_buffer = jsScript.read()
                    #when the file is saved, Windows line endings are used (CRLF). When hashing these are changed to LF since the hash would change due to line endings
                    file_buffer = file_buffer.replace(WINDOWS_LINE_ENDINGS, UNIX_LINE_ENDINGS)
                    result = hashlib.sha256(file_buffer)
                    #print(result.hexdigest())
                    data = pd.read_excel(r"JQueryHashes.xlsx")
                    df = pd.DataFrame(data, columns=['Hash','Vulnerable'])
                    for index, row in df.iterrows():
                        #print(index, row['Hash'])
                        if row['Hash'] == result.hexdigest():
                            if row['Vulnerable'] == "Yes":
                                print("Vulnerable Library Detected from " + new_url + " "+ jsPath)
                                file = open(vulnerabilityReportPath, "a", encoding='utf-8')
                                file.write("\n--"+new_url+" | "+jsPath)
                                file.close()

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
