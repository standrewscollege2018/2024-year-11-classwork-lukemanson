# Format is [Car type, Seats, Availability]
import time
cars = [["Suzuki Van", 2, "", ""], ["Toyota Corolla", 4, "", ""], ["Honda CRV", 4, "", ""], ["Suzuki Swift", 4, "", ""], ["Mitsubishi Airtrek", 4, "", ""], ["Nissan DC Ute", 4, "", ""], ["Toyota Previa", 7, "", ""], ["Toyota Hi Ace", 12, "", ""], ["Toyota Hi Ace", 12, "", ""]]
while True:
    # Prints what vehicles exist
    print("Vehicles:")
    time.sleep(1)
    for i in range(len(cars)):
        time.sleep(0.5)
        print(f"{i+1}. {cars[i][0]} ({cars[i][1]}) {cars[i][2]}")
    time.sleep(1)
    temp_user_name = input("What is your name? ")
    temp_vehicle_booked = int(input("Which vehicle would you like to book? "))
    no_car_picked = True
    if temp_vehicle_booked == 0:
        break
    while no_car_picked:
        if cars[temp_vehicle_booked - 1][2] == "Unavailable":
            print("Please pick an available vehicle.")
            time.sleep(1)
            temp_vehicle_booked = int(input("Which vehicle would you like to book? "))
        else:
            print("Thank you for shopping with Briscoes.")
            no_car_picked = False
            cars[temp_vehicle_booked - 1][2] = "Unavailable"
            cars[temp_vehicle_booked - 1][3] = temp_user_name

