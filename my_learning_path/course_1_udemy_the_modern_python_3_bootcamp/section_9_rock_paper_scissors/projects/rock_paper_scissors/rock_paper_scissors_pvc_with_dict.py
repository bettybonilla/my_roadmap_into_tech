"""
The program below is a rock, paper, scissors game for PvC (Player vs. Computer)
"""

# Below the import keyword is used to import everything from the random module
# and the time module
# All imports should be done at the top of files
# The Python built-in random module generates pseudo-random numbers or
# elements based on the function used and the deterministic parameters set
import random
import time

ROCK = "r"
PAPER = "p"
SCISSORS = "s"

# The code below is a dictionary which points the computer's choice using the
# constants above from a letter ("r", "p", "s") to a word
# ("rock", "paper", "scissors")
# The constants below are the keys which point to the corresponding words
# which are the values (key -> value)
computer_dictionary = {
    ROCK: "rock",
    PAPER: "paper",
    SCISSORS: "scissors",
}

# The random.choice() function is used to generate a random element from the
# list [ROCK, PAPER, SCISSORS]
computer = random.choice([ROCK, PAPER, SCISSORS])

# -----------------------------------------------------------------------------
# The code below is alternative code to the code above
# Below the from ... import statement is used to specifically import the
# choice() function from the random module and used to generate a random
# element from the list [ROCK, PAPER, SCISSORS]
# from random import choice

# ROCK = "r"
# PAPER = "p"
# SCISSORS = "s"

# computer = choice([ROCK, PAPER, SCISSORS])
# -----------------------------------------------------------------------------

time.sleep(0.5)
print("Welcome!\n")

time.sleep(0.5)
print("rock?")
time.sleep(0.5)
print("paper?")
time.sleep(0.5)
print("scissors?")
time.sleep(0.5)
print("shoot!\n")
time.sleep(0.5)

player1 = input("Player 1, enter your choice: ").lower().strip()

if player1 == "":
    print("YOU DIDN'T ENTER ANYTHING, TRY AGAIN! >:-(")
    quit(1)
player1 = player1[0]
if player1 not in [ROCK, PAPER, SCISSORS]:
    print("YOU ENTERED GIBBERISH, TRY AGAIN! >:-(")
    quit(1)

# Prints the computer's choice on the same line after 0.5 sec
print("Computer, enter your choice:", end=" ", flush=True)
time.sleep(0.5)
print(computer_dictionary[computer])

if player1 == computer:
    print("It's a tie, play again! :-)")
elif player1 == ROCK and computer != PAPER:
    print("Player 1 wins!")
elif player1 == PAPER and computer != SCISSORS:
    print("Player 1 wins!")
elif player1 == SCISSORS and computer != ROCK:
    print("Player 1 wins!")
else:
    print("Computer wins!")
