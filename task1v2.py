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

# If-Statements to test whether the user or computer won using conditional and logical operators
if computerPlay == playerPlay:
    print("The computer is " + computerPlay + ".  You are " + playerPlay + "!")
    print("It was a tie!")
elif computerPlay == "Rock" and playerPlay == "Paper":
    print("The computer is Rock.  You are Paper!")
    print("You won!")
elif computerPlay == "Paper" and playerPlay == "Scissors":
    print("The computer is Paper.  You are Scissors!")
    print("You won!")
elif computerPlay == "Scissors" and playerPlay == "Rock":
    print("The computer is Scissors.  You are Rock!")
    print("You won!")
elif computerPlay == "Paper" and playerPlay == "Rock":
    print("The computer is Paper.  You are Rock!")
    print("You lost!")
elif computerPlay == "Scissors" and playerPlay == "Paper":
    print("The computer is Scissors.  You are Paper!")
    print("You lost!")
elif computerPlay == "Rock" and playerPlay == "Scissors":
    print("The computer is Rock.  You are Scissors!")
    print("You lost!")
else:
    print("You broke me!  How'd that happen?")
