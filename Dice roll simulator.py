import random

roll_again = "yes"
min_val = 1
max_val = 6
while roll_again == "yes" or roll_again == "y":
    print("Rolling the dices....")
    print(random.randint(min_val,max_val))
    print(random.randint(min_val,max_val))
    roll_again = input("Roll the dice again? ")
print("Thanks for playing!\nHave a great day ;)")