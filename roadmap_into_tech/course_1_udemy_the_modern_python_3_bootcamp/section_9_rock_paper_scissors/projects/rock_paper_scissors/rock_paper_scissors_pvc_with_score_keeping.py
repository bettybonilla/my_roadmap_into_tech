"""
The program below is a rock, paper, scissors game for PvC (Player vs. Computer)
- The player is able to choose the play mode by entering 1 for best 2 out of 3
mode or 0 for best 3 out of 5 mode
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

print("Play Modes")
time.sleep(0.5)
print("- Enter 1 for best 2 out of 3 mode")
print("- Enter 0 for best 3 out of 5 mode\n")
time.sleep(0.5)

play_mode_str = input("Please enter your play mode: ").strip()

if play_mode_str != "1" and play_mode_str != "0":
    print(
        "Invalid Input: Enter 1 for best 2 out of 3 mode or 0 for best 3 out of 5 mode"
    )
    quit(1)

play_mode_bool = bool(int(play_mode_str))
time.sleep(0.5)
print("")

player1_wins = 0
computer_wins = 0

while play_mode_bool == True:
    computer = random.choice([ROCK, PAPER, SCISSORS])
    # print(computer)

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

    while player1 == computer:
        print("It's a tie, play again! :-)")
        time.sleep(0.5)
        computer = random.choice([ROCK, PAPER, SCISSORS])
        # print(computer)

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

    if player1 == ROCK and computer != PAPER:
        print("Player 1 wins!")
        player1_wins += 1
        time.sleep(0.5)
        print("Score")
        time.sleep(0.5)
        print("- Player 1: {}".format(player1_wins))
        print("- Computer: {}".format(computer_wins))
        time.sleep(0.5)
    elif player1 == PAPER and computer != SCISSORS:
        print("Player 1 wins!")
        player1_wins += 1
        time.sleep(0.5)
        print("Score")
        time.sleep(0.5)
        print("- Player 1: {}".format(player1_wins))
        print("- Computer: {}".format(computer_wins))
        time.sleep(0.5)
    elif player1 == SCISSORS and computer != ROCK:
        print("Player 1 wins!")
        player1_wins += 1
        time.sleep(0.5)
        print("Score")
        time.sleep(0.5)
        print("- Player 1: {}".format(player1_wins))
        print("- Computer: {}".format(computer_wins))
        time.sleep(0.5)
    else:
        print("Computer wins!")
        computer_wins += 1
        time.sleep(0.5)
        print("Score")
        time.sleep(0.5)
        print("- Player 1: {}".format(player1_wins))
        print("- Computer: {}".format(computer_wins))
        time.sleep(0.5)

    if player1_wins == 2:
        print("Player 1 won best 2 out of 3 mode!")
        time.sleep(0.5)
        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again[0] == "y":
            time.sleep(0.5)
            player1_wins = 0
            computer_wins = 0
        elif play_again[0] == "n":
            time.sleep(0.5)
            print("Thanks for playing, Bye!")
            break
    if computer_wins == 2:
        print("Computer won best 2 out of 3 mode!")
        time.sleep(0.5)
        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again[0] == "y":
            time.sleep(0.5)
            player1_wins = 0
            computer_wins = 0
        elif play_again[0] == "n":
            time.sleep(0.5)
            print("Thanks for playing, Bye!")
            break

while play_mode_bool == False:
    computer = random.choice([ROCK, PAPER, SCISSORS])
    # print(computer)

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

    while player1 == computer:
        print("It's a tie, play again! :-)")
        time.sleep(0.5)
        computer = random.choice([ROCK, PAPER, SCISSORS])
        # print(computer)

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

    if player1 == ROCK and computer != PAPER:
        print("Player 1 wins!")
        player1_wins += 1
        time.sleep(0.5)
        print("Score")
        time.sleep(0.5)
        print("- Player 1: {}".format(player1_wins))
        print("- Computer: {}".format(computer_wins))
        time.sleep(0.5)
    elif player1 == PAPER and computer != SCISSORS:
        print("Player 1 wins!")
        player1_wins += 1
        time.sleep(0.5)
        print("Score")
        time.sleep(0.5)
        print("- Player 1: {}".format(player1_wins))
        print("- Computer: {}".format(computer_wins))
        time.sleep(0.5)
    elif player1 == SCISSORS and computer != ROCK:
        print("Player 1 wins!")
        player1_wins += 1
        time.sleep(0.5)
        print("Score")
        time.sleep(0.5)
        print("- Player 1: {}".format(player1_wins))
        print("- Computer: {}".format(computer_wins))
        time.sleep(0.5)
    else:
        print("Computer wins!")
        computer_wins += 1
        time.sleep(0.5)
        print("Score")
        time.sleep(0.5)
        print("- Player 1: {}".format(player1_wins))
        print("- Computer: {}".format(computer_wins))
        time.sleep(0.5)

    if player1_wins == 3:
        print("Player 1 won best 3 out of 5 mode!")
        time.sleep(0.5)
        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again[0] == "y":
            time.sleep(0.5)
            player1_wins = 0
            computer_wins = 0
        elif play_again[0] == "n":
            time.sleep(0.5)
            print("Thanks for playing, Bye!")
            break
    if computer_wins == 3:
        print("Computer won best 3 out of 5 mode!")
        time.sleep(0.5)
        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again[0] == "y":
            time.sleep(0.5)
            player1_wins = 0
            computer_wins = 0
        elif play_again[0] == "n":
            time.sleep(0.5)
            print("Thanks for playing, Bye!")
            break
