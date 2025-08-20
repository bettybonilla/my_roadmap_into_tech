"""
- The program below is a number guessing game for PvC (Player vs. Computer)
where the player has to guess the random number the computer picks between 1
and 10 and the computer gives hints to help the player guess the number by
stating if the number guessed was too high or too low
- The player is also asked if they would like to play again
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

# Generates a random number between 1 and 10 (inclusive)
computer = random.randint(1, 10)

# while True loops will loop forever until it hits the break keyword
while True:
    # Variable shadowing should be avoided which is when you re-use the same
    # exact variable name for altered data
    # When you validate data or in general alter data in any way, it's good
    # practice to rename variables separately with the altered data since the
    # raw data has been altered from the original variable and this way you can
    # still access the original variable with the unaltered raw data if needed
    # However, if you don't need to have 2 separate variables, you can also
    # cast the input() function inside the int() type conversion function
    # player_input = int(input("Guess the number between 1 and 10: ").strip())
    player_input_str = input("Guess the number between 1 and 10: ").strip()
    player_input_int = int(player_input_str)

    if player_input_int == computer:
        print("You guessed it! You win!")
        time.sleep(0.5)
        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        # Below is another way to look for user input by using the
        # .find() method for variables with string data types
        # The > -1 refers to looking for the string index of "y" in the user
        # input and if the string index of "y" is greater than -1, then
        # this means "y" would be found indexed 0 or greater in the user input
        # and would make the if conditional truthy which would execute the next
        # lines of code
        # The .strip() method above wouldn't be needed since the
        # .find() method will find the string regardless of whitespaces
        # if play_again.find("y") > -1:
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
