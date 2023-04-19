"""
The program below is a rock, paper, scissors game for PvP (Player vs. Player)
which clears the screen to deter cheating between the players
"""

import os

ROCK = "r"
PAPER = "p"
SCISSORS = "s"

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

# Clears the screen to deter cheating between the players
os.system("clear")

player2 = input("Player 2, enter your choice: ").lower().strip()

if player2 == "":
    print("YOU DIDN'T ENTER ANYTHING, TRY AGAIN! >:-(")
    quit(1)
player2 = player2[0]
if player2 not in [ROCK, PAPER, SCISSORS]:
    print("YOU ENTERED GIBBERISH, TRY AGAIN! >:-(")
    quit(1)

if player1 == player2:
    print("It's a tie, play again! :-)")
elif player1 == ROCK and player2 != PAPER:
    print("Player 1 wins!")
elif player1 == PAPER and player2 != SCISSORS:
    print("Player 1 wins!")
elif player1 == SCISSORS and player2 != ROCK:
    print("Player 1 wins!")
else:
    print("Player 2 wins!")
