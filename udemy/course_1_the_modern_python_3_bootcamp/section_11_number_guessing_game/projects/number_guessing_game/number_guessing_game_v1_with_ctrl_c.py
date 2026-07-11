"""
- The program below is a number guessing game for PvC (Player vs. Computer)
where the player has to guess the random number the computer picks between 1
and 10 and the computer gives hints to help the player guess the number by
stating if the number guessed was too high or too low
- The game will loop forever until the player presses Ctrl + C to exit the game
- NOTE: An alternative and good practice is to use the Python built-in atexit module
when signal handling so that it covers ALL exit signals to do graceful exits whereas
the below is only specific to the Ctrl + C exit signal
"""

import random
import signal
import time


# A Signal Handler is a defined function, as shown below, where Python signals
# can be handled
# Below, the signal_handler() function gracefully exits the program and
# provides an exit message to the player
def signal_handler(signum, frame):
    time.sleep(0.5)
    print("")
    print("Thanks for playing, Bye!")
    # Using exit(0) or quit(0) tells the program to exit/quit successfully
    # because there were no errors and also ensures that you terminate any
    # loops still running inside the program
    exit(0)


# The signal.SIGINT (SIGINT = Interrupt Signal AKA Ctrl + C) would be the
# default behavior to stop the current program running
# However, we can assign our own signal handler to detect this signal and do
# our custom processing instead
# Below, (signal.SIGINT, signal_handler) registers our
# signal_handler() function with signal.SIGINT (Ctrl + C)
# Therefore, after we run the program and press Ctrl + C, the program will go
# to our signal_handler() function
# https://www.askpython.com/python-modules/python-signal#:~:text=A%20Signal%20Handler%20is%20a,do%20our%20custom%20processing%20instead!
signal.signal(signal.SIGINT, signal_handler)

time.sleep(0.5)
print("Welcome!\n")

time.sleep(0.5)
print("Guess...")
time.sleep(0.5)
print("the...")
time.sleep(0.5)
print("number!\n")
time.sleep(0.5)

print("To exit the game, press Ctrl + C\n")
time.sleep(0.5)

# Generates a random number between 1 and 10 (inclusive)
computer = random.randint(1, 10)

# while True loops will loop forever until it hits the break keyword however
# since there is no break keyword, you have to press Ctrl + C to exit the
# program
while True:
    player_input_str = input("Guess the number between 1 and 10: ").strip()
    player_input_int = int(player_input_str)

    if player_input_int == computer:
        print("You guessed it! You win!")
        time.sleep(0.5)
        computer = random.randint(1, 10)
    elif player_input_int > computer:
        print("Too high, try again!")
    elif player_input_int < computer:
        print("Too low, try again!")
