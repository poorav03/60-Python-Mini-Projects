import  random

from scipy.stats import false_discovery_control
cpu_score=0
player_score=0
val = ["rock","Paper","Scissors"]

player = False
while True:
    player = input("Rock, Paper or Scissors?").capitalize()
    computer = random.choice(val)
    if player==computer:
        print("Tie!")
    elif player == "Rock":
        if(computer=="Paper"):
            print("You loose! ",computer," covers ",player)
            cpu_score+=1
        else:
            print("You win! ",player, " smashes ",computer)
            player_score+=1
    elif player == "Paper":
        if(computer=="Scissors"):
            print("You loose! ",computer," covers ",player)
            cpu_score+=1
        else:
            print("You win! ",player," smashes ",computer)
            player_score+=1
    elif player=="Scissors":
        if(computer=="Paper"):
            print("You loose! ",computer, " cuts ",player)
            cpu_score+=1
        else:
            print("You win! ",player," smashes ",computer)
            player_score+=1
    elif player=="End":
        print("Final scores:")
        print(f"CPU:{cpu_score}")
        print(f"PLAYER:{player_score}")
        break

