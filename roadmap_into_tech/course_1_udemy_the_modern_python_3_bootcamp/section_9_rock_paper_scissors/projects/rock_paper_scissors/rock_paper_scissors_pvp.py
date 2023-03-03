"""
The program below is a rock, paper, scissors game for PvP (Player vs. Player)
mode
"""

"""
- Constants are written at the top of files to be accessible throughout your
code below them
- It's a good idea to make something into a constant when you know you will be
repeating something throughout your code that won't change
- To implement string indexing with constants, make your constants equal to
the first character you expect in the string of the user input then reassign
the user input variables to equal the string index as shown below
    -  Ex: player1 = player1[0], player2 = player2[0]
    - This is an efficient way of string indexing which conserves memory since
    the string index for each user input variable will only be checked once
    instead of checking the string index for each user input variable
    repeatedly for each instance of the user input variable in the
    conditional logic below
"""

ROCK = "r"
PAPER = "p"
SCISSORS = "s"

print("Welcome!\n")
print("rock?\npaper?\nscissors?\nshoot!\n")

player1 = input("Player 1, enter your choice: ").lower().strip()

# This accounts for user input errors with empty strings from Player 1
if player1 == "":
    print("YOU DIDN'T ENTER ANYTHING, TRY AGAIN! >:-(")
    quit(1)
# This accounts for user input errors with gibberish from Player 1
# Using not in [ROCK, PAPER, SCISSORS] is the same as != ROCK and PAPER and
# SCISSORS
player1 = player1[0]
if player1 not in [ROCK, PAPER, SCISSORS]:
    print("YOU ENTERED GIBBERISH, TRY AGAIN! >:-(")
    quit(1)

player2 = input("Player 2, enter your choice: ").lower().strip()

# This accounts for user input errors with empty strings from Player 2
if player2 == "":
    print("YOU DIDN'T ENTER ANYTHING, TRY AGAIN! >:-(")
    quit(1)
# This accounts for user input errors with gibberish from Player 2
# Using not in [ROCK, PAPER, SCISSORS] is the same as != ROCK and PAPER and
# SCISSORS
player2 = player2[0]
if player2 not in [ROCK, PAPER, SCISSORS]:
    print("YOU ENTERED GIBBERISH, TRY AGAIN! >:-(")
    quit(1)

# It's best to place definite clear-cut logic at the top of your
# conditional logic to rule it out first since, if that condition is true, the
# rest of your code won't have to run which follows the return early rule
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

# =============================================================================
# The code below has been refactored to the code above
# ROCK = "r"
# PAPER = "p"
# SCISSORS = "s"

# print("Welcome!\n")
# print("rock?\npaper?\nscissors?\nshoot!\n")

# player1 = input("Player 1, enter your choice: ").lower().strip()
# if player1 == "":
#     print("YOU DIDN'T ENTER ANYTHING, TRY AGAIN! >:-(")
#     quit(1)

# player2 = input("Player 2, enter your choice: ").lower().strip()
# if player2 == "":
#     print("YOU DIDN'T ENTER ANYTHING, TRY AGAIN! >:-(")
#     quit(1)

# Reassigned the user input variables to equal the string index
# This is an efficient way of string indexing which conserves memory since
# the string index for each user input variable will only be checked once
# instead of checking the string index for each user input variable repeatedly
# for each instance of the user input variable in the conditional logic below
# player1 = player1[0]
# player2 = player2[0]

# It's best to place definite clear-cut logic at the top of your
# conditional logic to rule it out first since, if that condition is true, the
# rest of your code won't have to run which follows the return early rule
# if player1 == player2:
#     print("It's a tie, play again! :-)")
# elif player1 == ROCK and player2 != PAPER:
#     print("Player 1 wins!")
# elif player1 == PAPER and player2 != SCISSORS:
#     print("Player 1 wins!")
# elif player1 == SCISSORS and player2 != ROCK:
#     print("Player 1 wins!")
# else:
#     print("Player 2 wins!")
# =============================================================================
# The code below has been refactored to the code above
# print("Welcome!\n")
# print("rock?\npaper?\nscissors?\nshoot!\n")

# player1 = input("Player 1, enter your choice: ").lower().strip()
# if player1 == "":
#     print("YOU DIDN'T ENTER ANYTHING, TRY AGAIN! >:-(")
#     quit(1)

# player2 = input("Player 2, enter your choice: ").lower().strip()
# if player2 == "":
#     print("YOU DIDN'T ENTER ANYTHING, TRY AGAIN! >:-(")
#     quit(1)

# It's best to place definite clear-cut logic at the top of your
# conditional logic to rule it out first since, if that condition is true, the
# rest of your code won't have to run which follows the return early rule
# if player1 == player2:
#     print("It's a tie, play again! :-)")
# elif player1 == "rock" and player2 != "paper":
#     print("Player 1 wins!")
# elif player1 == "paper" and player2 != "scissors":
#     print("Player 1 wins!")
# elif player1 == "scissors" and player2 != "rock":
#     print("Player 1 wins!")
# else:
#     print("Player 2 wins!")
