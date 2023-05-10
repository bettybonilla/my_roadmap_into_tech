"""
- The program below is a number guessing game for PvC (Player vs. Computer)
where the player has to guess the random number the computer picks between 1
and 10 and the computer gives hints to help the player guess the number by
stating if the number guessed was too high or too low
- The player is able to choose the difficulty mode by entering 1 for easy mode
or 0 for hard mode
"""

import random
import time

time.sleep(0.5)
print("Welcome!\n")

time.sleep(0.5)
print("Guess...")
time.sleep(0.5)
print("the...")
time.sleep(0.5)
print("number!\n")
time.sleep(0.5)

"""
- The standard when writing terminal programs is to use 1 and 0 to represent
boolean True/False values (1 = True/truthy, 0 = False/falsy)
    - However if you're offering more than 2 options then you wouldn't be able
    to use boolean values
- Below double casting is used to cast the user input from a str to an int to
a bool
    - This allows you to use a while difficulty_mode_bool == True/False loops
    as opposed to while difficulty_mode_int == 1 or 2 loops as shown in the
    alternative code
    - Just using while True/False loops is not possible since you're pointing
    to the difficulty_mode_bool variable to look for the True/False value
"""

print("Difficulty Modes")
time.sleep(0.5)
print("- Enter 1 for easy mode (You get unlimited retries)")
print("- Enter 0 for hard mode (You only get 3 retries)\n")
time.sleep(0.5)

difficulty_mode_str = input("Please enter your difficulty mode: ").strip()

# Remember to place return early on errors logic right after where you expect
# the particular errors to occur to clearly define where the errors would
# originate and so that no other code executes without intention afterwards
if difficulty_mode_str != "1" and difficulty_mode_str != "0":
    print("Invalid Input: Enter 1 for easy mode or 0 for hard mode")
    quit(1)

difficulty_mode_bool = bool(int(difficulty_mode_str))
time.sleep(0.5)
print("")

# =============================================================================
# The code below is alternative code to the code above
# print("Enter 1 for easy mode")
# print("Enter 2 for hard mode\n")
# time.sleep(0.5)

# difficulty_mode_str = input("Please enter your difficulty mode: ").strip()
# difficulty_mode_int = int(difficulty_mode_str)
# time.sleep(0.5)
# print("")
# =============================================================================

# Generates a random number between 1 and 10 (inclusive)
computer = random.randint(1, 10)

retries = 3

# Alternative code to while difficulty_mode_bool == True loop
# while difficulty_mode_int == 1:
while difficulty_mode_bool == True:
    player_input_str = input("Guess the number between 1 and 10: ").strip()
    player_input_int = int(player_input_str)

    if player_input_int == computer:
        print("You guessed it! You win!")
        time.sleep(0.5)
        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again[0] == "y":
            time.sleep(0.5)
            computer = random.randint(1, 10)
        elif play_again[0] == "n":
            time.sleep(0.5)
            print("Thanks for playing, Bye!")
            break
    elif player_input_int > computer:
        print("Too high, try again!")
    elif player_input_int < computer:
        print("Too low, try again!")

# Alternative code to while difficulty_mode_bool == False loop
# while difficulty_mode_int == 2:
while difficulty_mode_bool == False:
    player_input_str = input("Guess the number between 1 and 10: ").strip()
    player_input_int = int(player_input_str)
    retries -= 1

    if player_input_int == computer:
        print("You guessed it! You win!")
        time.sleep(0.5)
        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again[0] == "y":
            time.sleep(0.5)
            computer = random.randint(1, 10)
            retries = 3
        elif play_again[0] == "n":
            time.sleep(0.5)
            print("Thanks for playing, Bye!")
            break
    elif player_input_int > computer and retries != 0:
        print("Too high, try again!")
        time.sleep(0.5)
        print("Retries left ({})".format(retries))
    elif player_input_int < computer and retries != 0:
        print("Too low, try again!")
        time.sleep(0.5)
        print("Retries left ({})".format(retries))
    elif retries == 0:
        print("Sorry, no more retries :-(")
        time.sleep(0.5)
        print("Thanks for playing, Bye!")
        break
