''' Example of connecting to a database and running queries '''

####### This is the setup stuff that will appear on every program #######

# Start by importing the sqlite3 library
import sqlite3
# Set the database that we will connect to
DATABASE = "cars.db"

# Connect to the database
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

# Run a query
cursor.execute("SELECT plate, owner, make, model, year, colour FROM car ORDER BY plate")
# Get results
results = cursor.fetchall()

# Print stuff
print("Plate                     Owner                     Make                      Model                     Year                      Colour")
print("="*150)
for car in results:
    print(f"{car[0]:<25} {car[1]:<25} {car[2]:<25} {car[3]:<25} {car[4]:<25} {car[5]:<25}")
