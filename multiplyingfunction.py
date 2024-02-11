''' This program demostrates how a function works '''
import math
import time

# Defines a function to multiply two numbers
def multiplier(a,b):
    return a * b


# User selects two integers to multiply
n1 = int(input("Please input an integer. "))
n2 = int(input("Please enter an integer to multiply the previous integer by. "))
calclength = math.ceil(math.log(multiplier(n1,n2)/10))
if calclength > 5:
    calclength = 5
# Calculating Cutscene
for i in range(calclength):
    for i in range(20):
        print("")
    print("Calculating.")
    time.sleep(0.5)
    for i in range(20):
        print("")
    print("Calculating..")
    time.sleep(0.5)
    for i in range(20):
        print("")
    print("Calculating...")
    time.sleep(0.5)
for i in range(20):
        print("")

# Multiplies them!
print("The answer is " + str(multiplier(n1,n2)) + ".")





