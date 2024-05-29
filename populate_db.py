import sqlite3
import random
import string

# Connect to the SQLite database
conn = sqlite3.connect('db.db')
cursor = conn.cursor()

# Function to generate random string
def generate_random_string(length=10):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

# Populate Artists table with 100 entries
for i in range(1, 101):
    cursor.execute("INSERT INTO artists (ID, Name, DateInit, DateEnd) VALUES (?, ?, ?, ?)",
                   (i, generate_random_string(), f"2022-01-01", f"2022-12-31"))

# Populate Users table with 100 entries
for i in range(1, 101):
    cursor.execute("INSERT INTO users (ID, Name, Email) VALUES (?, ?, ?)",
                   (i, generate_random_string(), f"{generate_random_string()}@example.com"))

# Populate ArtisticObject table with 100 entries
for i in range(1, 101):
    cursor.execute("INSERT INTO objects (ID, Name, Theme, Genre, Year, TypeArt, Material, AuthorID, ExecutorID, Owner) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (i, generate_random_string(), generate_random_string(), generate_random_string(), str(random.randint(1900, 2022)), generate_random_string(), generate_random_string(), random.randint(1, 100), random.randint(1, 100), generate_random_string()))

# Populate Logs table with 100 entries
for i in range(1, 101):
    cursor.execute("INSERT INTO logs (ObjectID, ArtistID) VALUES (?, ?)",
                   (random.randint(1, 100), random.randint(1, 100)))

# Commit changes to the database
conn.commit()

# Close the connection
conn.close()
