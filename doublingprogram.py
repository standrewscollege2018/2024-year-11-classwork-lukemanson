''' This program takes a number as input and doubles it! :')'''
import time
keep_asking = True
# Takes number as a float and asks again if the input is not a number
while keep_asking:
    try:
        n = float(input("Please enter a number. This program will double it. "))
        keep_asking = False
    except ValueError:
        time.sleep(1)
        print("")
        print("Please enter a number this time.")
        time.sleep(2)
        print("")
print("")
# Calculating Cutscene
for i in range(5):
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
# Print output
print("The result was " + str(2*n) + ".")
