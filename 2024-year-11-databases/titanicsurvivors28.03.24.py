''' Example of connecting to a database and running queries '''

####### This is the setup stuff that will appear on every program #######

# Start by importing the sqlite3 library
import sqlite3
# Set the database that we will connect to
DATABASE = "tItAnIC.db"

# Connect to the database
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

# Defining Variables
requested_class = 0
requested_alive = 1
quit_not_entered = True
while quit_not_entered:
    # Get inputs
    requested_class = input("What class do you want to search on? (1-3) ")
    requested_alive = input("Enter 1 for list of survivors or 0 for deceased: ")
    # Run the query
    cursor.execute("SELECT name FROM passengers WHERE class = ? AND survived = ?", (requested_class,requested_alive))
    # Get results
    results = cursor.fetchall()
    print(f"There are {len(results)} results found")
    for passenger in results:
        print(f"{passenger[0]}")
    if input("Press enter if you want to continue searching, otherwise, enter the word 'quit'. ") == "quit":
        quit_not_entered = False
