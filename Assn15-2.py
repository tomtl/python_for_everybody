import json
import sqlite3

def create_db_cursor() :
    connection = sqlite3.connect("rosterdb.sqlite")
    cursor = connection.cursor()
    return (connection, cursor)

def drop_tables_from_db(cursor) :
    cursor.executescript('''
        DROP TABLE IF EXISTS User;
        DROP TABLE IF EXISTS Course;
        DROP TABLE IF EXISTS Member;
    ''')

def create_user_table(cursor) :
    cursor.execute('''
        CREATE TABLE User (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            name TEXT UNIQUE
        )
    ''')

def create_course_table(cursor) :
    cursor.execute('''
        CREATE TABLE Course (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            title TEXT UNIQUE
        )
    ''')

def create_member_table(cursor) :
    cursor.execute('''
        CREATE TABLE Member (
            user_id INTEGER,
            course_id INTEGER,
            role INTEGER,
            PRIMARY KEY (user_id, course_id)
        )
    ''')

def reset_db(cursor) :
    drop_tables_from_db(cursor)
    create_user_table(cursor)
    create_course_table(cursor)
    create_member_table(cursor)

def get_input_data() :
    input_filename = raw_input("Enter file name:") or "roster_data.json"
    string_data = open(input_filename).read()
    json_data = json.loads(string_data)
    return json_data

def add_user_to_db(name, cursor) :
    cursor.execute(
        "INSERT OR IGNORE INTO User (name) VALUES ( ? )", (name, )
    )
    cursor.execute("SELECT id FROM User WHERE name = ?", (name, ))
    user_id = cursor.fetchone()[0]
    return user_id

def add_course_to_db(course_title, cursor) :
    cursor.execute(
        "INSERT OR IGNORE INTO Course (title) VALUES ( ? )", (course_title, )
    )
    cursor.execute("SELECT id FROM Course WHERE title = ?", (course_title, ))
    course_id = cursor.fetchone()[0]
    return course_id

def add_member_to_db(user_id, course_id, role, cursor) :
    cursor.execute('''
        INSERT OR REPLACE INTO Member (user_id, course_id, role)
        VALUES (?, ?, ?)''',
        (user_id, course_id, role)
    )

def add_enrollment_record_to_db(enrollment_record, cursor) :
        user_name = enrollment_record[0]
        course_title = enrollment_record[1]
        user_role = enrollment_record[2]

        user_id = add_user_to_db(user_name, cursor)
        course_id = add_course_to_db(course_title, cursor)
        add_member_to_db(user_id, course_id, user_role, cursor)

json_data = get_input_data()
connection, cursor = create_db_cursor()
reset_db(cursor)

print "Writing records to database..."
record_count = 0
for enrollment_record in json_data :
    add_enrollment_record_to_db(user_name, course_title, user_role, cursor)
    record_count += 1
    connection.commit()

print "Added %s records." % record_count
