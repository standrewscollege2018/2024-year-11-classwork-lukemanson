''' This program enables users to add students to the database '''

####### This is the setup stuff that will appear on every program ############

# Start by importing the sqlite3 library
import sqlite3

# Set the database that we will connect to
DATABASE = "students-TABLET-P1U6O80K.db"

# Connect to the database
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

#### Menu system for the program #######
run_program = True
while run_program:
    print("Main Menu")
    print("=========")
    print("1. Add student")
    print("2. Search for student")
    print("3. See all students")
    print("4. Update student")
    print("5. Quit")

    # get menu selection
    get_selection = True
    while get_selection:
        try:
            selection = int(input("Enter selection: "))
            if selection < 1 or selection > 5:
                print("You must enter a number from 1-5")
            else:
                get_selection = False
        except ValueError:
            print("Only numbers from 1-5 allowed.")

    # Now that we have the selection, do what the user wants

    ### Add student ###
    if selection == 1:
        print("\nAdd new student")
        first_name = input("First name: ")
        last_name = input("Last name: ")
        tutor_group = input("Tutor group: ")
        city = input("City: ")
        get_year_group = True
        while get_year_group:
            try:
                year_group = int(input("Year group: "))
                if year_group < 0:
                    print("Please enter a non-negative year group.")
                else:
                    get_year_group = False
            except ValueError:
                print("Please enter an integer year group.")
        cursor.execute("INSERT INTO student (firstName, lastName, tutorGroup, city, yearGroup) VALUES (?, ?, ?, ?, ?)", (first_name, last_name, tutor_group, city, year_group))
        # You must add connection.commit() or else the changes will not be saved when you stop the program
        connection.commit()

    ### Search for a student ###
    elif selection == 2:
        print("\nSearch for a student")
        search = input("Enter name: ")
        search_like = f"%{search}%"
        cursor.execute("SELECT * FROM student WHERE firstName LIKE ? OR lastName LIKE ?", (search_like, search_like))
        results = cursor.fetchall()
        if len(results) == 0:
            print("No results found")
        else:
            print(f"{'First name':15} {'Last name':15} {'Tutor group':6}")
            for student in results:
                print(f"{student[1]:15} {student[2]:15} {student[3]:6}")

    ### Show all students ###
    elif selection == 3:
        print("\nAll students: ")
        cursor.execute("SELECT * FROM student")
        results = cursor.fetchall()
        for student in results:
            print(f"{student[0]:5}. {student[1]:12} {student[2]:12} {student[3]:6} {student[4]:15} {student[5]:8}")

    ### Update a student ###
    elif selection == 4:
        print("\nUpdate a student")
        update = input("Enter name: ")
        update_like = f"%{update}%"
        cursor.execute("SELECT * FROM student WHERE firstName LIKE ? OR lastName LIKE ?", (update_like, update_like))
        results = cursor.fetchall()
        if len(results) == 0:
            print("No results found")
        else:
            print(f"{'First name':15} {'Last name':15} {'Tutor group':6}")
            for student in results:
                print(f"{student[1]:15} {student[2]:15} {student[3]:6}")

    ### Quit program ###
    else:
        run_program = False
