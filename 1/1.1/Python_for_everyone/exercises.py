# Counting Organizations
# This application will read the mailbox data (mbox.txt) and count the number of email messages per organization (i.e. domain name of the email address) using a database with the following schema to maintain the counts.

# CREATE TABLE Counts (org TEXT, count INTEGER)

import sqlite3
import re

# opening the files (database.sqlite and mbox.txt)
FILE = 'mbox.txt'

# opening or creating database file
conn = sqlite3.connect('data/organization.sqlite')
cur = conn.cursor()

# opening mbox.txt
fhand = open(FILE, "r")

# setup the database file for processing
# Deleting existing tables if they exist and creating a new one
cur.execute("DROP TABLE IF EXISTS Counts")
cur.execute("""
    CREATE TABLE Counts(
        org TEXT UNIQUE,
        count INTEGER
    )
""")

# Process the mail to and add to database
search = re.compile(r'^From: ([\w]+@[\w.]+)')
for line in fhand:
    # find all the emails from the file
    line = search.search(line)
    if line is None: continue
    org = line.group().split('@')[1]
    
    # check to see if the org already exists on the database
    cur.execute("SELECT count FROM Counts WHERE org = ?", (org,))
    row = cur.fetchone()
    if row is None:
        # this is the first occurance of email
        cur.execute("INSERT INTO Counts (org, count) VALUES (?,1)", (org,))
    else:
        # there is already org registered so increase the count
        cur.execute("UPDATE Counts SET count = count + 1 WHERE org = ?", (org,))
conn.commit()
cur.close()
