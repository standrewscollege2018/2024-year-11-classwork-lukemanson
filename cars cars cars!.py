''' This program allows users to enter their name and borrow a car from the list. If a car is borrowed it becomes unavailable and cannot be selected anymore.
    At the end of the day, the user enters "0" to finish the program and print the summary, which contains who borrowed the vehicles from the university. '''
import time
# Format is [Car type, Seats, Availability]
cars = [["Suzuki Van", 2, ""], ["Toyota Corolla", 4, ""], ["Honda CRV", 4, ""], ["Suzuki Swift", 4, ""], ["Mitsubishi Airtrek", 4, ""], ["Nissan DC Ute", 4, ""], ["Toyota Previa", 7, ""], ["Toyota Hi Ace", 12, ""], ["Toyota Hi Ace", 12, ""]]
# Format is [Car, Name]
vehicles_and_names = []
while True:
    # Prints what vehicles exist
    print("Vehicles:")
    time.sleep(1)
    for i in range(len(cars)):
        time.sleep(0.5)
        print(f"{i+1}. {cars[i][0]} ({cars[i][1]}) {cars[i][2]}")
    time.sleep(1)
    # Asks for the user's name which cannot be blank
    while True:
        temp_user_name = input("What is your name? ")
        if temp_user_name.strip() == "":
            time.sleep(1)
            print("Please do not enter a blank name.")
            time.sleep(1)
        else:
            break
    # Asks which vehicle the user wants to book which cannot be non-integer, blank, or out of the range 1-9
    while True:
        try:
            temp_vehicle_booked = int(input("Which vehicle would you like to book? "))
            # If in range then accept the selection and move to the next stage of checking
            if temp_vehicle_booked > -1 and temp_vehicle_booked < 10:
                break
            # If out of range re-ask
            else:
                time.sleep(1)
                print("Please enter a number from the list of cars.")
                time.sleep(1)
        # If not an integer
        except ValueError:
            time.sleep(1)
            print("Please enter an integer representing what car on the list you wish to borrow.")
            time.sleep(1)
    no_car_picked = True
    # Exits the while loop if 0 is entered (end of day)
    if temp_vehicle_booked == 0:
        break
    # Gets the user to enter an available vehicle
    while no_car_picked:
        # If the vehicle is booked re-ask
        if cars[temp_vehicle_booked - 1][2] == "Unavailable":
            print("Please pick an available vehicle.")
            time.sleep(1)
            temp_vehicle_booked = int(input("Which vehicle would you like to book? "))
        # Otherwise move on to the next person
        else:
            print("Thank you for shopping with Briscoes.")
            time.sleep(1)
            for i in range(5):
                print("")
            time.sleep(1)
            no_car_picked = False
            cars[temp_vehicle_booked - 1][2] = "Unavailable"
            vehicles_and_names.append([cars[temp_vehicle_booked - 1][0], temp_user_name])
for i in range(20):
    print("")
# Prints a summary showing all vehicles booked in that day
print("Daily Summary")
time.sleep(2)
for i in range(len(vehicles_and_names)):
    print(f"{vehicles_and_names[i-1][0]} - {vehicles_and_names[i-1][1]}")
    time.sleep(1)
if len(vehicles_and_names) == 0:
    print("No vehicles were borrowed today!")
