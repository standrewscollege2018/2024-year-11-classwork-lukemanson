""" Example of connecting to a database and running queries """

####### This is the setup stuff that will appear on every program #######

# Start by importing the sqlite3 library
import sqlite3

# Set the database that we will connect to
DATABASE = "premierleague.db"

# Connect to the database
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

# Defining Variables
quit_not_entered = True
slelection_not_entered = True

# Loopity Loop
while quit_not_entered:
    # The Menu
    while slelection_not_entered:
        try:
            slelection = int(input("\nMenu - Select from 1-6\n################################################################\n1. View all statistics tabulated\n2. See the teams with the highest average age\n3. See each team's possesion stats\n4. See which teams scored the most goals\n5. See which teams outperformed their expected goals by the most\n6. Quit the program\n"))
            if slelection > 6 or slelection < 1:
                print("Please enter a selection between 1 and 6. Your selection was outside the valid range.")
            else:
                slelection_not_entered = False
        except ValueError:
            print("Please enter a selection between 1 and 6. Your selection was not an integer.")
    slelection_not_entered = True

    # The user wants to view all stats (Case 1)
    if slelection == 1:
        cursor.execute("SELECT * FROM pl")
        results = cursor.fetchall()
        print("\n########################TABLE OF STATS#########################")
        print("Team                Average Age  Possession  Goals  Assists  xG")
        for team in results:
            print(f"{team[0]:15} {team[1]:13} {team[2]:12} {team[3]:6} {team[4]:6} {team[5]:6}")

    # The user want to see what teams are the oldest
    if slelection == 2:
        cursor.execute("SELECT team, average_age FROM pl ORDER BY average_age DESC")
        results = cursor.fetchall()
        print("\n##########AGE TABLE###########")
        print("Team               Average Age")
        for team in results:
            print(f"{team[0]:20} {team[1]:6}")

    # The user wants to see what teams have the highest possession
    if slelection == 3:
        cursor.execute("SELECT team, possession FROM pl ORDER BY possession DESC")
        results = cursor.fetchall()
        print("\n##########POSSESSION TABLE###########")
        print("Team               Average Possession")
        for team in results:
            print(f"{team[0]:22} {team[1]:6}%")

    # The user wants to see what teams scored the most goals
    if slelection == 4:
        cursor.execute("SELECT team, goals FROM pl ORDER BY goals DESC")
        results = cursor.fetchall()
        print("\n##########GOALS TABLE###########")
        print("Team               Goals Scored")
        for team in results:
            print(f"{team[0]:19} {team[1]:6}")

    # The user wants to see which teams outperformed their expected goals by the most
    if slelection == 5:
        cursor.execute("SELECT team, goals, xG, (goals - xG) AS diff FROM pl")
        results = cursor.fetchall()
        print("\n###############EXPECTED GOALS TABLE################")
        print("Team               Goals Scored   xG     Difference")
        for team in results:
            print(f"{team[0]:19} {team[1]:6} {team[2]:10} {round(team[3], 1):10}")

    # If the user selected "Quit", quit the program.
    if slelection == 6:
        quit_not_entered = False
        print("Goodbye!")
