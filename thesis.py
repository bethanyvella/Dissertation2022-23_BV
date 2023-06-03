#imports
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

#connecting to the database
conn = sqlite3.connect('dissertation_database.db')
cursor = conn.cursor()

#functions

# this function gets all the cdn stored in the database
def getCDN():
    cursor.execute("SELECT url.url, version.isVulnerable \
                    FROM url INNER JOIN variant on url.variantID = variant.variantID \
                    INNER JOIN version on version.versionID = variant.versionID \
                    WHERE version.isVulnerable == 1 ")

# this function is going to print out the results if there is a match
def printCDNResults(currentWebsiteUrl, currentScript):
    print("--------Vulnerable Library Detected from CDN:  " + currentWebsiteUrl)
    VulnFileWriter = open(vulnerabilityReportPath, "a", encoding='utf-8')
    VulnFileWriter.write("\n-- CDN: "+currentWebsiteUrl+" | "+ currentScript['src'])
    VulnFileWriter.close()  

# this function will get the scraped script and save it into a file
def fileWriting(jsFileNamePath, scrapedScriptContent):
    fileDiff = open(jsFileNamePath, "w", encoding='utf-8')
    fileDiff.write(scrapedScriptContent)
    fileDiff.close()
    with open(jsFileNamePath, 'rb') as jsScript:
        file_buffer = jsScript.read()
        #when the file is saved, Windows line endings are used (CRLF). When hashing these are changed to LF since the hash would change due to line endings
        windowsLineEndingsHash = hashlib.sha256(file_buffer).hexdigest() 
        file_LineEndingsReplaced = file_buffer.replace(WINDOWS_LINE_ENDINGS, UNIX_LINE_ENDINGS)
        unixLineEndingsHash = hashlib.sha256(file_LineEndingsReplaced).hexdigest() 
    return windowsLineEndingsHash, unixLineEndingsHash

# this function gets all the vulnerable hashed keys from db
def getHashKeys():
    cursor.execute("SELECT variant.hashKey, version.isVulnerable \
                    FROM variant \
                    INNER JOIN version on variant.versionID = version.versionID \
                    WHERE version.isVulnerable == 1") 

# this function prints out the hash results
def printHashResultsVuln(currentWebsiteUrl, currentScript):
    print("Vulnerable Library Detected from HASH:  " + currentWebsiteUrl)
    VulnFileWriter = open(vulnerabilityReportPath, "a", encoding='utf-8')
    VulnFileWriter.write("\n--HASH: "+currentWebsiteUrl+" | "+currentScript['src'])
    VulnFileWriter.close()

# this function will return all the vulnerable versions and paths from db, the code will open the path and match with scraped data
def getContent():
    cursor.execute("SELECT variant.content,  version.isVulnerable \
                    FROM variant \
                    INNER JOIN version on variant.versionID = version.versionID \
                    WHERE version.isVulnerable == 1") 

def diffChecking(currentContentVersion, jsFileNamePath ):
    biggestMatch = 0
    file =  ''.join(currentContentVersion)
    #open file from row
    with open (file, "r") as f:
        file1_lines = f.read()
        #diff url file with db file, get magic num %
    with open (jsFileNamePath, "r") as f:
        file2_lines = f.read()
    #keep track of biggest %
    sm=SequenceMatcher(a=file1_lines, b=file2_lines)
    if(sm.ratio() > biggestMatch):
        biggestMatch = sm.ratio()
    
    return biggestMatch, file  

#this function will print the difference results
def printDiffResults(biggestMatch, biggestatchString, jsFileNamePath, file):
    print("Biggest Match for files " + jsFileNamePath + " and " +file + " is: " + biggestatchString)
    VulnFileWriter = open(vulnerabilityReportPath, "a", encoding='utf-8')
    filePathFull = str(file)
    VulnFileWriter.write("\n--Biggest Match for files "+ jsFileNamePath + " and " + filePathFull + " is: " +biggestatchString)
    VulnFileWriter.close()

#reading from the Tranco list
readTrancoList = open('C:\\Users\\G\\Desktop\\WebScrapingProject1\\top1m.csv')
csv_reader = csv.reader(readTrancoList)

#setting constants
WINDOWS_LINE_ENDINGS = b'\r\n'
UNIX_LINE_ENDINGS = b'\n'

#setting logging level to info
logging.basicConfig(filename="logfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='a')
logger = logging.getLogger()
logger.setLevel(logging.INFO) 

#creating folder Websites to store the websites inside it
parentDirectory = "C:\\Users\\G\\Desktop\\WebScrapingProject1\\"
websiteFolderDirectory = "websites\\"
websiteFolderPath = os.path.join(parentDirectory, websiteFolderDirectory)
os.mkdir(websiteFolderPath)

#creating a vulnerability text file 
vulnerabilityReportPath = os.path.join(parentDirectory, "VulnerabilityReport.txt")
VulnFileWriter = open(vulnerabilityReportPath, "w", encoding='utf-8')
VulnFileWriter.write("--Vulnerability Report-- \n")
VulnFileWriter.close()

#setting useragent header
headers= {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

#starting to loop through CSV file where the list of websites are stored
for count, url in enumerate(csv_reader):
    currentWebsiteUrl = url[0]
    if(count == 50): 
        print("--End of Report--")
        VulnFileWriter = open(vulnerabilityReportPath, "a", encoding='utf-8')
        VulnFileWriter.write("--End of Report-- \n")
        VulnFileWriter.close()
        break

    try:
        #creating a folder for the current website
        currentWebsiteFolderPath = os.path.join(websiteFolderPath, currentWebsiteUrl)
        #opening as the current path
        os.mkdir(currentWebsiteFolderPath)
        
        #getting the response for the current website
        res = requests.get('http://' + currentWebsiteUrl, data=None, headers=headers).text
        #scraping the data
        soup = BeautifulSoup(res, 'html.parser')
        #getting all the scripts
        allScrapedScripts = soup.select('script')


        #setting the file number for the current website to 0
        websiteFileNumber = 0
        for currentScript in allScrapedScripts:
            hashMatch = False
            try: 
                #getting the scripts that has the <src> tag and that start with http
                if (currentScript.has_attr('src')) and (currentScript['src'].startswith("http")):
                    #getting the javascript/content for the current script url
                    jsOfCurrentScript = requests.get(currentScript['src']) 

                    #getting the vulnerable CDN urls saved in the database amd matchning them with retrieved Url from scraped website
                    getCDN()
                    allCdnInDB = cursor.fetchall()
                    for thisCDN in allCdnInDB:
                        currentCDN = thisCDN[0]
                        if currentCDN == currentScript['src']: 
                            printCDNResults(currentWebsiteUrl, currentScript)
                            break
                    
                    #if Url matching does not work, get file contents and hash match
                    #contruct file path so it could be saved
                    jsFileNamePath = currentWebsiteFolderPath + "\\" + currentScript['src'].replace(':', '_').replace('/', '_').replace('?', '_')

                    getResponse = requests.get(currentScript['src'])
                    scrapedScriptContent = getResponse.text
                    #writing the scrapedScript into a file so it could be hashed and later on diff checked.
                    windowsLineEndingsHash, unixLineEndingsHash  = fileWriting(jsFileNamePath, scrapedScriptContent)

                    #getting the vulnerable hashed keys from the database 
                    getHashKeys() 
                    allHashKeysInDB = cursor.fetchall()
                    # going through the vuln keys and match them
                    for thisHash in allHashKeysInDB:
                        currentHash = thisHash[0]
                        #the below statment is checked the scraped hash key wether it is with windows line endings or with unix line endings
                        #the program is returning both hash keys since some websites use one and some use others. therefore this program can catch both
                        if currentHash == windowsLineEndingsHash or currentHash == unixLineEndingsHash: 
                            printHashResultsVuln(currentWebsiteUrl, currentScript)
                            hashMatch = True
                            break

                    #if not match was found with hash keys, move onto the diff checking
                    if hashMatch == False:     
                        #getting all file content to match with scraped file 
                        getContent()
                        allContentinDB = cursor.fetchall()
                        for thisContnetVersion in allContentinDB:
                            currentContentVersion = thisContnetVersion[0]

                            #checking if scraped file matches one of the files in db
                            biggestMatch, file = diffChecking(currentContentVersion, jsFileNamePath)
                            #converting the number to string so it could be outputted in file
                            biggestatchString = str(biggestMatch)  
                        printDiffResults(biggestMatch,biggestatchString, jsFileNamePath, file)
                        
                        
                #if the js is found in between tags like so:<script> code here </script>        
                else:
                    #getting the script text to save in the file 
                    scrapedScriptContent = currentScript.text       
                    #create a new folder for un named scripts
                    websiteFileNumber +=1
                    jsFileNamePath = currentWebsiteFolderPath + "\\" + str(websiteFileNumber)
                    
                    windowsLineEndingsHash, unixLineEndingsHash  = fileWriting(jsFileNamePath,scrapedScriptContent)
                    #getting the vulnerable hashed keys from the database 
                    getHashKeys() 
                    allHashKeysInDB = cursor.fetchall()
                    # going through the vuln keys and match them
                    for thisHash in allHashKeysInDB:
                        currentHash = thisHash[0]
                        #the below statment is checked the scraped hash key wether it is with windows line endings or with unix line endings
                        #the program is returning both hash keys since some websites use one and some use others. therefore this program can catch both
                        if currentHash == windowsLineEndingsHash or currentHash == unixLineEndingsHash: 
                            printHashResultsVuln(currentWebsiteUrl, currentScript)
                            hashMatch = True
                            break

                    #if not match was found with hash keys, move onto the diff checking
                    if hashMatch == False:     
                        #getting all file content to match with scraped file 
                        getContent()
                        allContentinDB = cursor.fetchall()
                        for thisContnetVersion in allContentinDB:
                            currentContentVersion = thisContnetVersion[0]

                            #checking if scraped file matches one of the files in db
                            biggestMatch, file = diffChecking(currentContentVersion, jsFileNamePath)
                            #converting the number to string so it could be outputted in file
                            biggestatchString = str(biggestMatch)  
                        printDiffResults(biggestMatch,biggestatchString, jsFileNamePath, file)
                        
            except Exception as e:
                logger.error(e)
                continue
            except urllib.error.HTTPError as e:
                logger.error(e)
            except urllib.error.URLError as e:
                #print(new_url, 'FAILED:', e.reason)
                logger.error("Url Error - Website URL: %s Reason: %s",currentWebsiteUrl, e.reason)
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

    #exceptions        
    except Exception as e:
        logger.error(e)
        continue
    except urllib.error.HTTPError as e:
        logger.error(e)
    except urllib.error.URLError as e:
        #print(new_url, 'FAILED:', e.reason)
        logger.error("Url Error - Website URL: %s Reason: %s",currentWebsiteUrl, e.reason)
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
