# Set up boolean
stop_not_entered = True
# Set up list
names = []
# While the user is still entering names ask for more
while stop_not_entered:
    name = input()
    try:
        # Check if they enter the word stop to end the while loop
        if name.lower().strip(" ") == "stop":
            # Change the boolean to exit the while loop
            stop_not_entered = False
        # Check if the name is blank
        elif name.strip(" ") == "":
            print("Please do not enter a blank value")
        else:
            # Tests if the name is an integer, if it is not, sends you to error catching (ValueError)
            name = float(name)
            # Tells you off (naughty naughty)
            print("Please enter a non-numerical value")
    # If the name is valid:
    except ValueError:
        # Add the name to the list!
        names.append(name)
# Sorts each name!
names = sorted(names)
# Prints each name!
for i in range(len(names)):
    print(f"{i+1}. {names[i]}")
