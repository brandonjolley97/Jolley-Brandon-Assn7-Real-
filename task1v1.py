
import random


# Introducing the game.
print("Let's play Rock, Paper, Scissors!")

# Defining the necessary variables.  User input and randomly generated computer input
computerPlay = random.randint(0,2)
playerPlay = eval(input("Please enter a number 0-2. (0)Rock, (1)Paper, (2)Scissors: "))

# Changing random computer result to Rock, Paper, or Scissors
if computerPlay == 0:
    computerPlay = "Rock"
elif computerPlay == 1:
    computerPlay = "Paper"
else:
    computerPlay = "Scissors"

# Changing the user input to Rock, Paper, or Scissors
if playerPlay == 0:
    playerPlay = "Rock"
elif playerPlay == 1:
    playerPlay = "Paper"
elif playerPlay == 2:
    playerPlay = "Scissors"
else:
    print("Your input was incorrect!  Please try again.")

# If-Statements to test whether the user or computer won using only conditional operators.
if computerPlay == "Rock":
    if playerPlay == "Rock":
        print("The computer is Rock.  You are Rock too!")
        print("It was a draw!")
    elif playerPlay == "Paper":
        print("The computer is Rock.  You are Paper!")
        print("You won!")
    else:
        print("The computer is Rock.  You are Scissors!")
        print("You lost!")
elif computerPlay == "Paper":
    if playerPlay == "Rock":
        print("The computer is Paper.  You are Rock!")
        print("You lost!")
    elif playerPlay == "Paper":
        print("The computer is Paper.  You are Paper too!")
        print("It was a draw!")
    else:
        print("The computer is Paper.  You are Scissors!")
        print("You won!")
elif computerPlay == "Scissors":
    if playerPlay == "Rock":
        print("The computer is Scissors.  You are Rock!")
        print("You won!")
    elif playerPlay == "Paper":
        print("The computer is Scissors.  You are Paper!")
        print("You lost!")
    else:
        print("The computer is Scissors.  You are Scissors too!")
        print("It was a draw!")
else:
    print("You broke me!  How'd that happen?")


