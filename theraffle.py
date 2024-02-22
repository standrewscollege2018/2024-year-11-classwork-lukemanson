import time
from random import randint
time.sleep(1)
print("Why hello there, raffle holder!")
time.sleep(1)
prize = input("What is the prize of your raffle? ")
while prize.lower().strip() == "":
    print("Please do not enter an empty name.")
    prize = input("What is the prize of your raffle? ")
time.sleep(1)
ok_prize = False
prize_value = input("What is the value of that prize? ")
while ok_prize == False:
    try:
        if prize_value.lower().strip() == "":
            print("Please do not enter an empty name.")
            prize_value = input("What is the value of that prize? ")
        elif float(prize_value) > 0 or float(prize_value) == 0:
            ok_prize = True
        else:
            print("Please enter a non-negative value.")
            prize_value = input("What is the value of that prize? ")
    except ValueError:
        print(f'Please enter a number for the value. "{prize_value}" is not a number.')
        prize_value = input("What is the value of that prize? ")
time.sleep(1)
print('Now, please enter the names of people in the draw. Enter one name, then press enter. Repeat until you have entered all names, then type "end".')
end_not_entered = True
name = ""
names = []
while end_not_entered:
    time.sleep(1)
    name = input("Please enter a name. ")
    if name.lower().strip(" ") == "":
        print("Please do not enter an empty name.")
        time.sleep(1)
    elif name.lower().strip(" ") == "end":
        end_not_entered = False
    else:
        names.append(name)
if len(names) == 0:
    haha = True
else:
    rando = randint(0, len(names) - 1)
time.sleep(1)
for i in range(20):
    print("")
pointless_variable = input("Press enter to begin the raffle. ")
time.sleep(1)
if len(names) == 0:
    print(f"There are no people in the draw.")
elif len(names) == 1:
    print(f"There is one person in the draw.")
else:
    print(f"There are {len(names)} people in the draw.")
time.sleep(1)
print(f"The prize for the raffle is: {prize}.")
time.sleep(1)
if len(names) == 0:
    print("No names means no winner!")
elif len(names) == 1:
    print(f"Well, it could only really be {names[rando]}!")
else:
    print(f"The winner is: {names[rando]}")
