''' Example of connecting to a database and running queries '''

####### This is the setup stuff that will appear on every program #######

# Start by importing the sqlite3 library
import sqlite3
# Set the database that we will connect to
DATABASE = "cars.db"

# Connect to the database
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

####### Get plate from user and run search #######
plate = input("Enter plate number: ")

# This search requires an EXACT match
cursor.execute("SELECT plate, owner FROM car WHERE plate = ?", (plate,))
# Get results
results = cursor.fetchall()

# This is a fuzzy search, looks fo plates that INCLUDE the variable
# We need to pre-prepare the variable!!!!1!11!!!1!1! (important)
like_plate = f"%{plate}%"
cursor.execute("SELECT plate, owner FROM car WHERE plate LIKE ?", (like_plate,))

results = cursor.fetchall()

# Print results
for car in results:
    print(f"Plate: {car[0]:>10}. Owner: {car[1]:>20}.")

name = input("Name: ")
model = input("Model: ")
cursor.execute("SELECT plate, owner FROM car WHERE owner = ? AND model = ?", (name,model))
results = cursor.fetchall()

for car in results:
    print(f"Name: {car[0]:>10}. Model: {car[1]:>20}.")

