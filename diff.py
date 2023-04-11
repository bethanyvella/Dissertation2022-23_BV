from difflib import Differ, SequenceMatcher
import sqlite3
import os

scrapedJS = 'C:\\Users\\betha\\Desktop\\ITProject-Dissertation\\JQueries\\3.0.0\\uncompressed\\jquery-3.6.0.js'
#open & read url file

conn = sqlite3.connect('dissertation_database.db')
cursor = conn.cursor()
biggestMatch = 0
for row1 in (cursor.execute("SELECT content FROM variant")):
    file_path = row1
    file =  ''.join(file_path)
    print(file)
    #open file from row
    with open (file, "r") as f:
        file1_lines = f.read()
        #diff url file with db file, get magic num %
    with open (scrapedJS, "r") as f:
        file2_lines = f.read()
    #keep track of biggest %
    sm=SequenceMatcher(a=file1_lines, b=file2_lines)
    if(sm.ratio() > biggestMatch):
        biggestMatch = sm.ratio() 
    
    result = biggestMatch , " from " , file_path
    print(result)
#print closest match
