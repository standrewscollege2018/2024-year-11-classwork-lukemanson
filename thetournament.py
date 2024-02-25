''' This code allows the user to input their team name and the names of their opponents. Then, the user
inputs the result against each opponent, and the program checks whether it was a win, loss, or draw. The
program then calculates the total points for the team where a win is 3, a draw is 2, and a loss is 1. It
then prints the result to the user. '''
print("Hello user!")
team_name = input("What is the name of the team that is competing? ")
temp_opponent_var
opponents = []
done_not_entered = True
print('Please enter the names of opposition teams. Finish by entering "done".')
while done_not_entered:
    temp_opponent_var = input("Enter the name of an opponent.")
    try:
        if temp_opponent_var.strip() == "":
            print("Please do not enter a blank opponent name.")
        elif float(temp_opponent_var) == 0 or float(temp_opponent_var) == not 0:
            print("Please enter a non-numerical team name.")
    except ValueError:
        if temp_opponent_var.strip() == "done":
            done_not_entered = False
        else:
            opponents.append(temp_opponent_var)
    temp_opponent_var = ""
