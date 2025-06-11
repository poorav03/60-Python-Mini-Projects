def check_guess(guess,answer):
    global score
    attempt=0
    still_guessing = True
    while  still_guessing and attempt<3:
        if guess.lower() == answer.lower():
            print("Correct Answer")
            score = score+1
            still_guessing = False
        else:
            if attempt<2:
                guess = input("Sorry, Wrong answer Try again: ")
            attempt = attempt+1
    if attempt == 3:
        print("Correct answer is: ",answer)
score = 0
print("Guess the Animal!")

guess1 = input("Which bear lives at the North Pole? ")
check_guess(guess1, "polar bear")

guess2 = input("Which is the fastest land animal? ")
check_guess(guess2, "cheetah")

guess3 = input("Which is the largest animal? ")
check_guess(guess3, "blue whale")

guess4 = input("Which animal is known as the king of the jungle? ")
check_guess(guess4, "lion")

guess5 = input("Which bird is known for its ability to mimic human speech? ")
check_guess(guess5, "parrot")

guess6 = input("Which animal is the tallest in the world? ")
check_guess(guess6, "giraffe")

guess7 = input("Which marine creature has eight legs? ")
check_guess(guess7, "octopus")

guess8 = input("Which flightless bird is native to Antarctica? ")
check_guess(guess8, "penguin")

guess9 = input("Which animal is famous for playing dead as a defense mechanism? ")
check_guess(guess9, "opossum")

guess10 = input("Which animal is known for building dams? ")
check_guess(guess10, "beaver")

print("Your Score is: ",score)