import xml.etree.ElementTree as ET
import sqlite3

def drop_tables(cursor) :
    cursor.execute("DROP TABLE IF EXISTS Artist")
    cursor.execute("DROP TABLE IF EXISTS Genre")
    cursor.execute("DROP TABLE IF EXISTS Album")
    cursor.execute("DROP TABLE IF EXISTS Track")

def add_artist_table(cursor) :
    cursor.execute('''
        CREATE TABLE Artist (
            id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            name    TEXT UNIQUE
        )'''
    )

def add_genre_table(cursor) :
    cursor.execute('''
        CREATE TABLE Genre (
            id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            name    TEXT UNIQUE
        )'''
    )

def add_album_table(cursor) :
    cursor.execute('''
        CREATE TABLE Album (
            id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            artist_id  INTEGER,
            title   TEXT UNIQUE
        )'''
    )

def add_track_table(cursor) :
    cursor.execute('''
        CREATE TABLE Track (
            id  INTEGER NOT NULL PRIMARY KEY
                AUTOINCREMENT UNIQUE,
            title TEXT  UNIQUE,
            artist_id INTEGER,
            album_id  INTEGER,
            genre_id  INTEGER,
            len INTEGER,
            rating INTEGER,
            count INTEGER
        )'''
    )

def reset_db(cursor) :
    drop_tables(cursor)
    add_artist_table(cursor)
    add_genre_table(cursor)
    add_album_table(cursor)
    add_track_table(cursor)

def lookup(dictionary, key):
    found = False
    for child in dictionary:
        if found :
            return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

def add_artist_to_db(artist, cursor) :
    cursor.execute (
        "INSERT OR IGNORE INTO Artist (name) VALUES ( ? )", (artist, )
    )
    cursor.execute("SELECT id FROM Artist WHERE name = ?", (artist, ))
    artist_id = cursor.fetchone()[0]
    return artist_id

def add_album_to_db(album, cursor) :
    cursor.execute (
        "INSERT OR IGNORE INTO Album (title, artist_id) VALUES ( ?, ? )",
        (album, artist_id )
    )
    cursor.execute("SELECT id FROM Album WHERE title = ?", (album, ))
    album_id = cursor.fetchone()[0]
    return album_id

def add_genre_to_db(genre, cursor) :
    cursor.execute(
        "INSERT OR IGNORE INTO Genre (name) VALUES ( ? )", (genre, )
    )
    cursor.execute("SELECT id FROM Genre WHERE name = ?", (genre, ))
    genre_id = cursor.fetchone()[0]
    return genre_id

file_name = raw_input("Enter file name:") or "Library.xml"
input_data = ET.parse(file_name)
track_data = input_data.findall("dict/dict/dict")

connection = sqlite3.connect("tracks.sqlite")
cursor = connection.cursor()
reset_db(cursor)

track_count = 0
for track in track_data :
    if (lookup(track, "Track ID") is None) :
        continue

    name = lookup(track, 'Name')
    artist = lookup(track, 'Artist')
    album = lookup(track, 'Album')
    genre = lookup(track, 'Genre')
    count = lookup(track, 'Play Count')
    rating = lookup(track, 'Rating')
    length = lookup(track, 'Total Time')

    if name is None or artist is None or album is None or genre is None:
        continue

    artist_id = add_artist_to_db(artist, cursor)
    album_id = add_album_to_db(album, cursor)
    genre_id = add_genre_to_db(genre, cursor)

    cursor.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, artist_id, len, rating, count, genre_id)
        VALUES ( ?, ?, ?, ?, ?, ?, ? )''',
        ( name, album_id, artist_id, length, rating, count, genre_id ) )

    connection.commit()
    track_count += 1

print "Added %s tracks" % track_count
