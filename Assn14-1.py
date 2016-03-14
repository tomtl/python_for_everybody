import sqlite3

connection = sqlite3.connect('emaildb.sqlite')
cur = connection.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

file_name = raw_input("Enter filename:") or "mbox-short.txt"
file_handler = open(file_name)

domain_counts = {}
for line in file_handler :
    if not line.startswith("From: ") :
        continue

    words = line.split()
    email_address = words[1]
    email_domain = email_address.split("@")[1]

    domain_counts[email_domain] = domain_counts.get(email_domain, 0) + 1
