"""
The program below is a rock, paper, scissors game for PvC (Player vs. Computer)
mode
"""

# Imports the built-in Python random module which generates pseudo-random
# numbers or elements based on the function or method used and the
# deterministic parameters set - All imports should be done at the top of files
# Below the import keyword is used to import everything from the random module
# and the random.choice() method is used to generate a random element from the
# list [ROCK, PAPER, SCISSORS]
import random

ROCK = "r"
PAPER = "p"
SCISSORS = "s"

computer = random.choice([ROCK, PAPER, SCISSORS])

# ============================================================================
# The code below is alternative code to the code above
# Below the from ... import statement is used to specifically import the
# choice() function from the random module and used to generate a random
# element from the list [ROCK, PAPER, SCISSORS]
# from random import choice

# ROCK = "r"
# PAPER = "p"
# SCISSORS = "s"

# computer = choice([ROCK, PAPER, SCISSORS])
# ============================================================================

print("Welcome!\n")
print("rock?\npaper?\nscissors?\nshoot!\n")

player1 = input("Player 1, enter your choice: ").lower().strip()

if player1 == "":
    print("YOU DIDN'T ENTER ANYTHING, TRY AGAIN! >:-(")
    quit(1)
player1 = player1[0]
if player1 not in [ROCK, PAPER, SCISSORS]:
    print("YOU ENTERED GIBBERISH, TRY AGAIN! >:-(")
    quit(1)

print("Computer, enter your choice:", computer)

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
