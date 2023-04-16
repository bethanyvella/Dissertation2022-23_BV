from ast import Compare
import imp
from msilib.schema import File
from urllib import response
from bs4 import BeautifulSoup
import requests
import urllib.request
import csv 
import pandas as pd
import logging
import os
import urllib3
from urllib3.exceptions import NewConnectionError
import hashlib
from difflib import Differ, SequenceMatcher
import sqlite3
import os

conn = sqlite3.connect('dissertation_database.db')
cursor = conn.cursor()

readTrancoList = open('C:\\Users\\betha\\Desktop\\ITProject-Dissertation\\WebScrapingProject\\top1m.csv')
csv_reader = csv.reader(readTrancoList)
WINDOWS_LINE_ENDINGS = b'\r\n'
UNIX_LINE_ENDINGS = b'\n'

logging.basicConfig(filename="logfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='a')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

parent_dir = "C:\\Users\\betha\\Desktop\\ITProject-Dissertation\\WebScrapingProject\\"
directory = "websites2\\"
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
    if(count == 100): 
        break
    
    try:
        path2 = os.path.join(path1, new_url)
        os.mkdir(path2)
    
        headers= {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}
        req = requests.get('http://' + new_url, data=None, headers=headers).text
        soup = BeautifulSoup(req, 'html.parser')
        server = soup.select('server')
        #print(new_url, server)
        scripts = soup.select('script')
        filenumber = 0
        for s in scripts:
        #-----------------------------------------------------------------------------------
        # CDN MATCH     
            if s.has_attr('src'):
                if s['src'].startswith("http"):
                    js = requests.get(s['src']) 

                    #getting the URL data from DB
                    cursor.execute("SELECT url.url, version.isVulnerable \
                    FROM url INNER JOIN variant on url.variantID = variant.variantID \
                    INNER JOIN version on version.versionID = variant.versionID")            
                    rowsCDN = cursor.fetchall()

                    
                    for dataCDN in rowsCDN:
                        url_CDN_data = dataCDN[0]
                        isVuln = dataCDN[1]
                        if url_CDN_data == s['src']:
                            if isVuln == 1:
                                print("--------Vulnerable Library Detected from CDN:  " + new_url + jsPath)
                                file = open(vulnerabilityReportPath, "a", encoding='utf-8')
                                file.write("\n--"+new_url+" | "+jsPath)
                        else:
                            if s['src'][0] != "/":
                                js = requests.get("http://"+new_url+"/"+s['src'])
                                if url_CDN_data == s['src']:
                                    if isVuln == 1:
                                        print("--------Vulnerable Library Detected from CDN:  " + new_url + jsPath)
                                        file = open(vulnerabilityReportPath, "a", encoding='utf-8')
                                        file.write("\n--"+new_url+" | "+jsPath)
                            else:
                                js = requests.get("http://"+new_url+s['src'])
                                if url_CDN_data == s['src']:
                                    if isVuln == 1:
                                        print("--------Vulnerable Library Detected from CDN:  " + new_url + jsPath)
                                        file = open(vulnerabilityReportPath, "a", encoding='utf-8')
                                        file.write("\n--"+new_url+" | "+jsPath)
                    #--------------------------------------------------------------------------------------
                    #HASH MATCH
                    jsPath = path2 + "\\" + s['src'].replace(':', '_').replace('/', '_').replace('?', '_')
                    file = open(jsPath, "w", encoding='utf-8')
                    file.write(js.text)
                    file.close()
                    with open(jsPath, 'rb') as jsScript:
                        file_buffer = jsScript.read()
                        #when the file is saved, Windows line endings are used (CRLF). When hashing these are changed to LF since the hash would change due to line endings
                        file_buffer = file_buffer.replace(WINDOWS_LINE_ENDINGS, UNIX_LINE_ENDINGS)
                        result = hashlib.sha256(file_buffer)
                        
                        cursor.execute("SELECT variant.hashKeys, version.isVulnerable \
                                        FROM variant \
                                        INNER JOIN version on variant.versionID = version.versionID ") 
                        rowsHash = cursor.fetchall()
                        for dataHash in rowsHash:
                                hash_data = dataHash[0]
                                isVuln = dataHash[1]

                                if hash_data == result.hexdigest():
                                    if isVuln == 1:
                                        print("Vulnerable Library Detected from HASH:  " + new_url + jsPath)
                                        file = open(vulnerabilityReportPath, "a", encoding='utf-8')
                                        file.write("\n--"+new_url+" | "+jsPath)
                                        file.close()
                                else:
                                    biggestMatch = 0
                                    cursor.execute("SELECT variant.content,  version.isVulnerable \
                                                    FROM variant \
                                                    INNER JOIN version on variant.versionID = version.versionID ")
                                    rowContent = cursor.fetchall()
                                    for dataContent in rowContent:
                                        content_data = dataContent[0]
                                        isVuln = dataContent[1]

                                        file =  ''.join(content_data)
                                        print(file)
                                        #open file from row
                                        with open (file, "r") as f:
                                            file1_lines = f.read()
                                            #diff url file with db file, get magic num %
                                        with open (jsPath, "r") as f:
                                            file2_lines = f.read()
                                        #keep track of biggest %
                                        sm=SequenceMatcher(a=file1_lines, b=file2_lines)
                                        if(sm.ratio() > biggestMatch):
                                            biggestMatch = sm.ratio() 
                                        
                                        result = biggestMatch , " from " , content_data
                                        print(result)
                        
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
                        
                        cursor.execute("SELECT variant.hashKeys, version.isVulnerable \
                                        FROM variant \
                                        INNER JOIN version on variant.versionID = version.versionID ") 
                        rowsHash = cursor.fetchall()
                        for dataHash in rowsHash:
                                hash_data = dataHash[0]
                                isVuln = dataHash[1]

                                if hash_data == result.hexdigest():
                                    if isVuln == 1:
                                        print("Vulnerable Library Detected from HASH: " + new_url + " "+ jsPath)
                                        file = open(vulnerabilityReportPath, "a", encoding='utf-8')
                                        file.write("\n--"+new_url+" | "+jsPath)
                                        file.close()
                                else:
                                    biggestMatch = 0
                                    cursor.execute("SELECT variant.content,  version.isVulnerable \
                                                    FROM variant \
                                                    INNER JOIN version on variant.versionID = version.versionID ")
                                    rowContent = cursor.fetchall()
                                    for dataContent in rowContent:
                                        content_data = dataContent[0]
                                        isVuln = dataContent[1]

                                        file =  ''.join(content_data)
                                        print(file)
                                        #open file from row
                                        with open (file, "r") as f:
                                            file1_lines = f.read()
                                            #diff url file with db file, get magic num %
                                        with open (jsPath, "r") as f:
                                            file2_lines = f.read()
                                        #keep track of biggest %
                                        sm=SequenceMatcher(a=file1_lines, b=file2_lines)
                                        if(sm.ratio() > biggestMatch):
                                            biggestMatch = sm.ratio() 
                                        
                                        result = biggestMatch , " from " , content_data
                                        print(result)



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

