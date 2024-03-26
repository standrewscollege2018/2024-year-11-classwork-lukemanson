''' Example of connecting to a database and running queries '''

####### This is the setup stuff that will appear on every program #######

# Start by importing the sqlite3 library
import sqlite3
# Set the database that we will connect to
DATABASE = "students-TABLET-P1U6O80K.db"

# Connect to the database
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

# Run a query
cursor.execute("SELECT firstName, lastName, tutorGroup FROM student ORDER BY tutorGroup")
# Get results
results = cursor.fetchall()

# Loop over results list and display each result one at a time
for student in results:
    print(f"{student[0]:15} {student[1]:15} {student[2]:8}")
# OR this way
# for i in range(len(results)):
    # print(f"{results[i][0]} {results[i][1]}")
