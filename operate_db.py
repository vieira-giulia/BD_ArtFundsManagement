import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('db.db')
cursor = conn.cursor()

# Query artists alive
cursor.execute("""
    SELECT Name
    FROM artists
    WHERE DateEnd > '2019-12-31'
""")
alive_artists_2019 = cursor.fetchall()

# Display the result
print("\nArtists Alive:")
if alive_artists_2019:
    for artist in alive_artists_2019:
        print(artist[0])



# Update all artists alive to be dead
print("\nUpdate Artists Alive after 2019 to dead:")
cursor.execute("""
    UPDATE artists
    SET DateEnd = '2018-12-01'
    WHERE DateEnd > '2019-12-31'
""")
conn.commit()


# Query artists alive
cursor.execute("""
    SELECT Name
    FROM artists
    WHERE DateEnd > '2019-12-31'
""")
alive_artists_2019 = cursor.fetchall()

# Display the result
print("\nArtists Alive:")
if alive_artists_2019:
    for artist in alive_artists_2019:
        print(artist[0])

# Query to find the most visited artist by name
cursor.execute("""
    SELECT a.Name as ArtistName, COUNT(*) as VisitCount
    FROM Logs l
    JOIN artists a ON l.ArtistID = a.ID
    GROUP BY l.ArtistID
    ORDER BY VisitCount DESC
    LIMIT 1
""")
most_visited_artist = cursor.fetchone()

# Display the result
print("\nMost Visited Artist:")
print(f"Artist Name: {most_visited_artist[0]}, Visit Count: {most_visited_artist[1]}")


# Close the connection
conn.close()
