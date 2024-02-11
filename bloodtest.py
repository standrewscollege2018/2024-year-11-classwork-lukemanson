def check(a,w):
    try:
        if int(a) > 15 and int(w) > 49:
            return True
        else:
            return False
    except ValueError:
        return False

age = input("Please enter your age. ")
weight = input("Please enter your weight. ")
while check(age,weight) == False:
    age = int(input("Please enter your age. "))
    weight = int(input("Please enter your weight. "))

print("These are your details:  Age: " + str(age) + "   Weight: " + str(weight) + ". You can donate blood!")
