import sqlite3

def open_source_data() :
    # open source data file
    file_name = raw_input("Enter filename:") or "mbox.txt"
    file_handler = open(file_name)
    return file_handler

def count_domains(file) :
    # count email address domains in original data
    domain_counts = {}
    for line in file :
        if not line.startswith("From: ") :
            continue

        words = line.split()
        email_address = words[1]
        email_domain = email_address.split("@")[1]

        domain_counts[email_domain] = domain_counts.get(email_domain, 0) + 1
    return domain_counts

def connect_to_db(db_name) :
    # connect to sqlite db
    connection = sqlite3.connect(db_name)
    cur = connection.cursor()

    return (connection, cur)

def create_db_table(cursor) :
    # create sqlite table
    cursor.execute("DROP TABLE IF EXISTS Counts")
    cursor.execute("CREATE TABLE Counts (org TEXT, count INTEGER)")

def add_records_to_db(records_dictionary, connection, cursor) :
    # create records in sqlite table
    for key, value in records_dictionary.items() :
        cursor.execute('''
            INSERT INTO Counts (org, count)
            VALUES (?, ?)
        ''', (key, value))
        print "INSERT", key, value

    connection.commit()

def close_db(cursor) :
    cursor.close()

input_data = open_source_data()
domain_counts = count_domains(input_data)
connection, cursor = connect_to_db("emaildb.sqlite")
create_db_table(cursor)
add_records_to_db(domain_counts, connection, cursor)
close_db(cursor)
