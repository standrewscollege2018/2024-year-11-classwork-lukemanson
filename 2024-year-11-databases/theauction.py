''' Program running an auction '''

####### This is the setup stuff that will appear on every program ############

# Start by importing the sqlite3 library
import sqlite3

# Set the database that we will connect to
DATABASE = "auction.db"

# Connect to the database
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

print("Welcome to the auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction of auction")
# Part 1 - get all pre-info (name and reserve)
still_going_pt_1 = True
while still_going_pt_1:
    entering_name = True
    entering_reserve = True
    while entering_name:
        auctioner_name = input("\nWhat is the name of the item you are selling? Remember to never enter duplicate names! ")
        if auctioner_name.strip() == "":
            print("Please enter your name, not a blank.")
        else:
            entering_name = False
    while entering_reserve:
        try:
            reserve = float(input("What is the reserve price for your item, in NZD? "))
            if reserve < 0:
                print("Please enter a non-negative reserve price for your item.")
            else:
                entering_reserve = False
        except ValueError:
            print("Please enter a reserve price for your item. Your input was not a number.")
    cursor.execute("INSERT INTO item (name, reserve) VALUES (?, ?)", (auctioner_name, reserve))
    connection.commit()
    if input("Type 'y' to continue entering names and items, and 'n' to start the auction. ").strip() == "n":
        still_going_pt_1 = False


# Part 2 - Run the auction!
item_iterate = 0
cursor.execute("SELECT * FROM item")
results = cursor.fetchall()
for item in results:
    entering_purchaser = True
    entering_selling_price = True
    print(f"\n{item_iterate+1}. {item[1]} is selling for a reserve price of {item[2]}.")
    while entering_purchaser:
        purchaserer = input(f"Who purchased {item[1]}? ")
        if purchaserer.strip() == "":
            print("Please do not enter a blank purchaser. Try again! ")
        else:
            entering_purchaser = False

    while entering_selling_price:
        try:
            selling_price = input(f"How much in NZD did {purchaserer} purchase {item[1]} for? If there was no purchaser, enter 'Unsold'. ")
            float_price = float(selling_price)
            if float_price >= reserve:
                if len(results) == item_iterate + 1:
                    print("That's all the items!")
                else:
                    print("Ok, onto the next item!")
                entering_selling_price = False
            else:
                print("That selling price is too low. Please enter a selling price above the reserve.")
        except ValueError:
            if selling_price.lower().strip() == "unsold":
                print(":(")
                entering_selling_price = False
            else:
                print("Please enter a valid number.")

    item_iterate += 1

# Update le stuff
e = input("")
for i in range(item_iterate):
    cursor.execute("UPDATE item SET purchaser = ?, salePrice = ? WHERE name = ?", (purchaserer, selling_price, auctioner_name))
e = input("")
# Finally, clear the table!
cursor.execute("DELETE FROM item")
connection.commit()
