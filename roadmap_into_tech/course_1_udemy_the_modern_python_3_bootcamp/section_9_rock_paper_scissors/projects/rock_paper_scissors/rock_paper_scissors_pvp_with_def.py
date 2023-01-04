# ============================================================================
# TODO Revisit and test knowledge
# ============================================================================

ROCK = "r"
PAPER = "p"
SCISSORS = "s"


# Checks the player input to see if it's valid
def is_input_valid(player_input):
    if player_input == "":
        return (False, "YOU DIDN'T ENTER ANYTHING, TRY AGAIN! >:-(")

    if player_input[0] not in [ROCK, PAPER, SCISSORS]:
        return (False, "YOU ENTERED GIBBERISH, TRY AGAIN! >:-(")

    return (True, "")


# Compares input to see who is the winner
def compare_input(player1, player2):
    # This is the only logic i added, it makes sure that we are always
    # comparing the first letter only
    if len(player1) > 1:
        player1 = player1[0]

    if len(player2) > 1:
        player2 = player2[0]

    message = ""
    if player1 == player2:
        message = "It's a tie, play again! :-)"
    elif player1 == ROCK and player2 != PAPER:
        message = "Player 1 wins!"
    elif player1 == PAPER and player2 != SCISSORS:
        message = "Player 1 wins!"
    elif player1 == SCISSORS and player2 != ROCK:
        message = "Player 1 wins!"
    else:
        message = "Player 2 wins!"
    return message


# Runs the code below only if you run the python command on this file
if __name__ in '__main__':
    print("Welcome!\n")
    print("rock?\npaper?\nscissors?\nshoot!\n")

    player1 = input("Player 1, enter your choice: ").lower().strip()
    valid, error_message = is_input_valid(player1)
    if not valid:
        print(error_message)
        quit(1)

    player2 = input("Player 2, enter your choice: ").lower().strip()
    valid, error_message = is_input_valid(player2)
    if not valid:
        print(error_message)
        quit(1)

    message_to_players = compare_input(player1[0], player2[0])
    print(message_to_players)
