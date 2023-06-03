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

#-----------------------------------------------------------------------functions------------------------------------------------------------------------------------


def getHashKeys():
    cursor.execute("SELECT variant.hashKey, version.isVulnerable \
                    FROM variant \
                    INNER JOIN version on variant.versionID = version.versionID ") 
    

def printHashResultsVuln(vulnerabilityReportPath):
    if isVuln == 1:
        print("Vulnerable Library Detected from HASH:  " + new_url + jsPath)
        VulnFileWriter = open(vulnerabilityReportPath, "a", encoding='utf-8')
        VulnFileWriter.write("\n--HASH: "+new_url+" | "+jsPath)
        VulnFileWriter.close()

def getCDN():
    cursor.execute("SELECT url.url, version.isVulnerable \
                    FROM url INNER JOIN variant on url.variantID = variant.variantID \
                    INNER JOIN version on version.versionID = variant.versionID")

def printCDNResults(new_url, jsPath):
    if isVuln == 1:
        print("--------Vulnerable Library Detected from CDN:  " + new_url +" " + jsPath)
        VulnFileWriter = open(vulnerabilityReportPath, "a", encoding='utf-8')
        VulnFileWriter.write("\n-- CDN: "+new_url+" | "+script['src'])
        VulnFileWriter.close()       

def fileWriting(js):
    fileDiff = open(jsPath, "w", encoding='utf-8')
    fileDiff.write(js.text)
    fileDiff.close()
    with open(jsPath, 'rb') as jsScript:
        file_buffer = jsScript.read()
        #when the file is saved, Windows line endings are used (CRLF). When hashing these are changed to LF since the hash would change due to line endings
        file_hash_result = hashlib.sha256(file_buffer).hexdigest() 
        file_buffer = file_buffer.replace(WINDOWS_LINE_ENDINGS, UNIX_LINE_ENDINGS)
    return file_hash_result 

def getContent():
    cursor.execute("SELECT variant.content,  version.isVulnerable \
                    FROM variant \
                    INNER JOIN version on variant.versionID = version.versionID ")
        
def diffChecking():
    biggestMatch = 0
    file =  ''.join(content_data)
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
    
    return biggestMatch, file  
    

def construct_url_and_get_js(script, new_url):
    full_url = "http://"+new_url
    if script['src'][0] != "/":
        full_url+="/"
    js = requests.get(full_url+script['src'])
    return js

#----------------------------------------------------------------------------main code -------------------------------------------------------------------------------
readTrancoList = open('C:\\Users\\betha\\Desktop\\ITProject-Dissertation\\WebScrapingProject\\top1m.csv')
csv_reader = csv.reader(readTrancoList)
WINDOWS_LINE_ENDINGS = b'\r\n'
UNIX_LINE_ENDINGS = b'\n'

logging.basicConfig(filename="logfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='a')
logger = logging.getLogger()
logger.setLevel(logging.INFO) #https://docs.python.org/3/library/logging.html#levels

parent_dir = "C:\\Users\\betha\\Desktop\\ITProject-Dissertation\\WebScrapingProject\\"
directory = "websites\\"
col1 = "JS Path"
col2 = "Hash"
path1 = os.path.join(parent_dir, directory)
os.mkdir(path1)
    
vulnerabilityReportPath = os.path.join(parent_dir, "VulnerabilityReport.txt")
VulnFileWriter = open(vulnerabilityReportPath, "w", encoding='utf-8')
VulnFileWriter.write("--Vulnerability Report-- \n")
VulnFileWriter.close()

headers= {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

for count, url in enumerate(csv_reader):
    new_url = url[0]
    if(count == 1000): 
        print("--End of Report--")
        VulnFileWriter = open(vulnerabilityReportPath, "a", encoding='utf-8')
        VulnFileWriter.write("--End of Report-- \n")
        VulnFileWriter.close()
        break
       
    try:
        path2 = os.path.join(path1, new_url)
        os.mkdir(path2)
    
        res = requests.get('http://' + new_url, data=None, headers=headers).text
        soup = BeautifulSoup(res, 'html.parser')
        server = soup.select('server')
        #print(new_url, server)
        all_scripts = soup.select('script')
        filenumber = 0
        for script in all_scripts:
            try: 
                hashMatch = False
            #-----------------------------------------------------------------------------------
            # CDN MATCH     
                if (script.has_attr('src')) and (script['src'].startswith("http")):
                    js_of_script = requests.get(script['src']) 
                    #getting the URL data from DB
                    getCDN()
                    all_cdn = cursor.fetchall()
                    for cdn in all_cdn:
                        url_CDN_data = cdn[0]
                        isVuln = cdn[1]
                        if url_CDN_data == script['src']:
                            printCDNResults(new_url, script['src'])

                        else:
                            #js = construct_url_and_get_js(script, new_url)
                            #if url_CDN_data == script['src']:
                                #printCDNResults()        
                            if script['src'][0] != "/":
                                js = requests.get("http://"+new_url+"/"+script['src'])
                                if url_CDN_data == script['src']:
                                    printCDNResults()
                            else:
                                js = requests.get("http://"+new_url+script['src'])
                                if url_CDN_data == script['src']:
                                    printCDNResults()
                    #--------------------------------------------------------------------------------------
                    #HASH MATCH
                    
                    #constructing the path to be saved in the local folder
                    jsPath = path2 + "\\" + script['src'].replace(':', '_').replace('/', '_').replace('?', '_')
                    #js = construct_url_and_get_js(script, new_url)
                    response = requests.get(script)
                    content = response.text

                    #writing scraped code in a file 
                    file_hash_result  = fileWriting(js)
                    #getting hash keys in database
                    getHashKeys() 
                    all_hashes = cursor.fetchall()
                    for hash in all_hashes:
                        hash_data = hash[0]
                        isVuln = hash[1]

                        #checking if hashed key matches a hash from db
                        if hash_data == file_hash_result : 
                            printHashResultsVuln(vulnerabilityReportPath)
                            hashMatch = True
                            break

                        
                        if hashMatch == False:     
                            #getting all file content to match with scraped file 
                            getContent()
                            rowContent = cursor.fetchall()
                            for dataContent in rowContent:
                                content_data = dataContent[0]
                                isVuln = dataContent[1]

                                #checking if scraped file matches one of the files in db
                                biggestMatch, file = diffChecking()
                                biggestatchString = str(biggestMatch)
                                if isVuln == 1:
                                    
                                    print("Biggest Match for files " + jsPath + " and " +file + " is: " + biggestatchString)
                                    VulnFileWriter = open(vulnerabilityReportPath, "a", encoding='utf-8')
                                    filePathFull = str(file)
                                    VulnFileWriter.write("\n--Biggest Match for files "+ jsPath + " and " + filePathFull + " is: " +biggestatchString)
                                    VulnFileWriter.close()
                else:
                    filenumber +=1
                    jsPath = path2 + "\\" + str(filenumber)
                    file_hash_result  = fileWriting(script)
                    #getting hash keys in database
                    getHashKeys()
                    all_hashes = cursor.fetchall()
                    for hash in all_hashes:
                        hash_data = hash[0]
                        isVuln = hash[1]

                        #checking if hashed key matches a hash from db
                        if hash_data == file_hash_result:
                            printHashResultsVuln(vulnerabilityReportPath)
                            hashMatch = True
                            break
                            
                        
                    if hashMatch == False:
                        #if it doesnt match, get file, and check with the difference tool
                        #getting all file content to match with scraped file 
                        getContent()
                        rowContent = cursor.fetchall()
                        for dataContent in rowContent:
                            content_data = dataContent[0]
                            isVuln = dataContent[1]

                            #checking if scraped file matches one of the files in db
                            biggestMatch, file = diffChecking()
                            biggestatchString = str(biggestMatch)
                            if isVuln == 1 and biggestMatch >= 80:
                                print("Biggest Match for files " + jsPath + " and " + file + " is: " + biggestatchString)
                                VulnFileWriter = open(vulnerabilityReportPath, "a", encoding='utf-8')
                                filePathFull = str(file)
                                VulnFileWriter.write("\n--Biggest Match for files "+ jsPath + " and "  + " is: " +biggestatchString)
                                VulnFileWriter.close()
                            
            except Exception as e:
                logger.error(e)
                #print('Something unexpected happened', str(e))
                continue
            except urllib.error.HTTPError as e:
                print(new_url , e.headers.get('Server'))
                logger.error(e)
            except urllib.error.URLError as e:
                #print(new_url, 'FAILED:', e.reason)
                logger.error("Url Error - Website URL: %s Reason: %s",new_url, e.reason)
            except ConnectionError as e:
                logger.error(e)
                continue
            except ConnectionResetError as e:
                logger.error(e)
                continue
            except TimeoutError as e:
                logger.error(e)
                continue
            except urllib3.exceptions.TimeoutError as e:
                logger.error(e)
                continue
            except NewConnectionError as e:
                logger.error(e)
                continue
            except requests.exceptions.ConnectionError as e:
                logger.error(e)
                continue


    except Exception as e:
        logger.error(e)
        #print('Something unexpected happened', str(e))
        continue
    except urllib.error.HTTPError as e:
        print(new_url , e.headers.get('Server'))
        logger.error(e)
    except urllib.error.URLError as e:
        #print(new_url, 'FAILED:', e.reason)
        logger.error("Url Error - Website URL: %s Reason: %s",new_url, e.reason)
    except ConnectionError as e:
        logger.error(e)
        continue
    except ConnectionResetError as e:
        logger.error(e)
        continue
    except TimeoutError as e:
        logger.error(e)
        continue
    except urllib3.exceptions.TimeoutError as e:
        logger.error(e)
        continue
    except NewConnectionError as e:
        logger.error(e)
        continue
    except requests.exceptions.ConnectionError as e:
        logger.error(e)
        continue


