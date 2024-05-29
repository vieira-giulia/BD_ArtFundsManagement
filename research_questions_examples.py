import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('db.db')

# Create a cursor object
cursor = conn.cursor()

# 1. Which Art Type is More Popular
cursor.execute("""
    SELECT TypeArt
    FROM objects
    JOIN logs ON objects.ID = logs.ObjectID
    GROUP BY TypeArt
    ORDER BY COUNT(*) DESC
    LIMIT 1;
""")
result_1 = cursor.fetchone()
print("\n1. Most Popular Art Type:", result_1[0] if result_1 else "No data")

# 2. Which Art Genre is More Popular
cursor.execute("""
    SELECT Genre
    FROM objects
    JOIN logs ON objects.ID = logs.ObjectID
    GROUP BY Genre
    ORDER BY COUNT(*) DESC
    LIMIT 1;
""")
result_2 = cursor.fetchone()
print("\n2. Most Popular Art Genre:", result_2[0] if result_2 else "No data")

# 3. The 5 Most Popular Artistic Objects
cursor.execute("""
    SELECT objects.*
    FROM objects
    JOIN logs ON objects.ID = logs.ObjectID
    GROUP BY objects.ID
    ORDER BY COUNT(*) DESC
    LIMIT 5;
""")
result_3 = cursor.fetchall()
print("\n3. The 5 Most Popular Artistic Objects:")
for row in result_3:
    print(row)

# 4. Owners of the 5 Most Popular Artistic Objects
cursor.execute("""
    SELECT objects.Owner
    FROM objects
    JOIN logs ON objects.ID = logs.ObjectID
    GROUP BY objects.Owner
    ORDER BY COUNT(*) DESC
    LIMIT 5;
""")
result_4 = cursor.fetchall()
print("\n4. Owners of the 5 Most Popular Artistic Objects:")
for owner in result_4:
    print(owner[0])

# 5. Locations of the 5 Most Popular Artistic Objects
cursor.execute("""
    SELECT objects.Owner
    FROM objects
    JOIN logs ON objects.ID = logs.ObjectID
    GROUP BY objects.Owner
    ORDER BY COUNT(*) DESC
    LIMIT 5;
""")
result_5 = cursor.fetchall()
print("\n5. Locations of the 5 Most Popular Artistic Objects:")
for location in result_5:
    print(location[0])

# 6. When Did Artistic Objects Receive More Visits in General
cursor.execute("""
    SELECT DATE(logs.Date) as VisitDate
    FROM logs
    GROUP BY VisitDate
    ORDER BY COUNT(*) DESC
    LIMIT 1;
""")
result_6 = cursor.fetchone()
print("\n6. Date with Most Visits:", result_6[0] if result_6 else "No data")

# Close the cursor and connection
cursor.close()
conn.close()
