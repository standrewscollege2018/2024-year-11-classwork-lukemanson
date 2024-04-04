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
class_not_accepted = True
alive_not_accepted = True
# Loop until quit is entered
while quit_not_entered:
    # Get inputs and error-catch
    while class_not_accepted:
        requested_class = input("What class do you want to search on? (1-3) ")
        try:
            if int(requested_class) < 1 or int(requested_class) > 3:
                print("Please enter a class from 1-3.")
            else:
                class_not_accepted = False
        except ValueError:
            print("Please enter a number between 1 and 3. It must have no letters and must be an integer.")
    class_not_accepted = True
    while alive_not_accepted:
        requested_alive = input("Enter 1 for list of survivors or 0 for deceased: ")
        try:
            if int(requested_alive) < 0 or int(requested_alive) > 1:
                print("Please enter either 0 or 1.")
            else:
                alive_not_accepted = False
        except ValueError:
            print("Please enter either 0 or 1. It must have no letters and must be an integer.")
    alive_not_accepted = True
    # Run the query
    cursor.execute("SELECT name FROM passengers WHERE class = ? AND survived = ?", (requested_class,requested_alive))
    # Get results
    results = cursor.fetchall()
    print(f"There are {len(results)} results found.")
    # Prints the list of passengers that meet the criteria
    for passenger in results:
        print(f"{passenger[0]}")
    # Asks the user if they want to continue searching or quit
    if input("Press enter if you want to continue searching, otherwise, enter the word 'quit'. ").lower().strip() == "quit":
        quit_not_entered = False
