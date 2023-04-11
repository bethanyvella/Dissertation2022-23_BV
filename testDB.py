from difflib import Differ, SequenceMatcher
import sqlite3


connection = sqlite3.connect('dissertation_database.db')
connection.execute("SELECT content FROM variant")
for row1 in (connection.execute("SELECT * FROM version")):
	print(row1)