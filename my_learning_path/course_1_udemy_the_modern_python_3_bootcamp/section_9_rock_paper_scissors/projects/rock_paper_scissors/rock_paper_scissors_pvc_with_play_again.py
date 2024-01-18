"""
The program below is a rock, paper, scissors game for PvC (Player vs. Computer)
- The player is also asked if they would like to play again
"""

import random
import time

ROCK = "r"
PAPER = "p"
SCISSORS = "s"

computer_dictionary = {
    ROCK: "rock",
    PAPER: "paper",
    SCISSORS: "scissors",
}

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

computer = random.choice([ROCK, PAPER, SCISSORS])

while True:
    player1 = input("Player 1, enter your choice: ").lower().strip()
    if player1 == "":
        print("YOU DIDN'T ENTER ANYTHING, TRY AGAIN! >:-(")
        quit(1)
    player1 = player1[0]
    if player1 not in [ROCK, PAPER, SCISSORS]:
        print("YOU ENTERED GIBBERISH, TRY AGAIN! >:-(")
        quit(1)

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

    time.sleep(0.5)
    play_again = input("Do you want to play again? (y/n): ").strip().lower()
    if play_again[0] == "y":
        time.sleep(0.5)
        computer = random.choice([ROCK, PAPER, SCISSORS])
    elif play_again[0] == "n":
        time.sleep(0.5)
        print("Thanks for playing, Bye!")
        break
