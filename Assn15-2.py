import json
import sqlite3

def create_db_cursor() :
    connection = sqlite3.connect("rosterdb.sqlite")
    cursor = connection.cursor()
    return cursor

def drop_tables_from_db(cursor) :
    cursor.executescript('''
        DROP TABLE IF EXISTS User;
        DROP TABLE IF EXISTS Course;
        DROP TABLE IF EXISTS Member;
    ''')

def reset_db(cursor) :
    drop_tables_from_db(cursor)
    # create user table
    # create course table
    # create member table

def get_input_data() :
    input_filename = raw_input("Enter file name:") or "roster_data.json"
    string_data = open(input_filename).read()
    json_data = json.loads(string_data)
    return json_data

json_data = get_input_data()
cursor = create_db_cursor()
reset_db(cursor)

# for entry in json_data :
    # add user
    # add course
    # add relationship
