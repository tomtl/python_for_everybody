import xml.etree.ElementTree as ET
import sqlite3

def lookup(dictionary, key):
    found = False
    for child in dictionary:
        if found :
            return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

file_name = raw_input("Enter file name:") or "Library.xml"
input_data = ET.parse(file_name)
track_data = input_data.findall("dict/dict/dict")

connection = sqlite3.connect("tracks.sqlite")
cursor = connection.cursor()

for track in track_data :
    if (lookup(track, "Track ID") is None) :
        continue

    name = lookup(track, 'Name')
    artist = lookup(track, 'Artist')
    album = lookup(track, 'Album')
    count = lookup(track, 'Play Count')
    rating = lookup(track, 'Rating')
    length = lookup(track, 'Total Time')

    if name is None or artist is None or album is None :
        continue

    print name, album, artist

    cursor.execute (
        "INSERT OR IGNORE INTO Artist (name) VALUES ( ? )", (artist, )
    )
    cursor.execute("SELECT id FROM Artist WHERE name = ?", (artist, ))
    artist_id = cursor.fetchone()[0]

    cursor.execute (
        "INSERT OR IGNORE INTO Album (title, artist_id) VALUES ( ?, ? )",
        (album, artist_id )
    )
    cursor.execute("SELECT id FROM Album WHERE title = ?", (album, ))
    album_id = cursor.fetchone()[0]

    cursor.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, len, rating, count)
        VALUES ( ?, ?, ?, ?, ? )''',
        ( name, album_id, length, rating, count ) )

    connection.commit()
