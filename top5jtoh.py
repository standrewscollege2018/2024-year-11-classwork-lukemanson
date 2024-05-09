''' This program allows the user to enter and edit their top 5 JToH towers. '''
# Create variables, lists, etc.
top_5 = []
quit_not_entered = True
valid_num_not_entered = True
slelection = 0
tower_name = ""
blank_entered = True
valid_num2_not_entered = True
yn_not_entered = True

# User enters their top 5
print("Enter your top 5 JToH towers in order: ")
for i in range(5):
    top_5.append(input(f"{i+1}. "))

# Loops through giving the user options
while quit_not_entered:
    # Gives the user a menu and allows them to enter a number
    while valid_num_not_entered:
        print("\nTop 5 JToH Towers Menu\n######################\n1. See the top 5\n2. Add a tower to the top 5\n3. Quit program")
        try:
            slelection = int(input("Selection: ").strip())
            if slelection < 1 or slelection > 3:
                print("Invalid selection. Please enter a number from 1 to 3.")
            else:
                valid_num_not_entered = False
        except ValueError:
            print("Please enter an integer from 1-3.")
    # This allows the user to see the top 5
    if slelection == 1:
        print("\nTop 5 JToH Towers\n=================")
        for i in range(len(top_5)):
            print(f"{i+1}. {top_5[i]}")

    # This allows the user to add a new item to the top 5, bumping off another item
    if slelection == 2:
        while blank_entered:
            print("\nAdd tower\n=========")
            tower_name = input("Tower name: ")
            if tower_name.strip() == "":
                print("Sorry, the tower name cannot be blank. Please try again.")
            else:
                blank_entered = False
                while valid_num2_not_entered:
                    try:
                        pos = int(input("What position in the top 5 (0 to return to the menu without adding): "))
                        if pos < 0 or pos > 5:
                            print("Please enter a position between 1-5, or 0 if you wish to exit to the menu.")
                        else:
                            valid_num2_not_entered = False
                            while yn_not_entered:
                                proceed = input(f"\nWARNING! This will remove {top_5[4]} from the top 5. Are you sure? (Y/N) ")
                                if proceed.lower().strip() == "y":
                                    yn_not_entered = False
                                    top_5.pop(4)
                                    top_5.insert(pos-1, tower_name)
                                    print(f"\nOkay, {tower_name} has been inserted into the top 5 in position 3.")
                                elif proceed.lower().strip() == "n":
                                    yn_not_entered = False
                                    print("That's OK, you are being returned to the menu.")
                                else:
                                    print("Please enter either Y or N to continue.")
                    except ValueError:
                        print("Please enter a valid number from 0-5.")

    if slelection == 3:
        quit_not_entered = False
        print("\nGoodbye!")

    # Reset variables for another loop through if necessary
    valid_num_not_entered = True
    blank_entered = True
    valid_num2_not_entered = True
    yn_not_entered = True
