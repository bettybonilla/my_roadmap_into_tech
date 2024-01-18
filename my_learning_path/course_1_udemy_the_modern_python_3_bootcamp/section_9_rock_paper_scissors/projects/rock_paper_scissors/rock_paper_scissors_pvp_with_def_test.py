# -----------------------------------------------------------------------------
# TODO Revisit and test knowledge
# -----------------------------------------------------------------------------

import io
import sys
import unittest

# Import definitions from your file
from rock_paper_scissors_pvp_with_def import is_input_valid, compare_input


# Stops print statements from showing up in terminal
def disable_print_statement_noise_in_test():
    suppress_text = io.StringIO()
    sys.stdout = suppress_text


def enable_print_statements_again():
    sys.stdout = sys.__stdout__


class MyTest(unittest.TestCase):
    def test_is_input_valid(self):
        testcases = [
            {
                "name": "empty string",
                "player_input": "",
                "expected_value": (False, "YOU DIDN'T ENTER ANYTHING, TRY AGAIN! >:-("),
            },
            {
                "name": "user entered gibberish, single letter",
                "player_input": "x",
                "expected_value": (False, "YOU ENTERED GIBBERISH, TRY AGAIN! >:-("),
            },
            {
                "name": "user entered gibberish, multi-letter",
                "player_input": "eszxdcfvgbhnj",
                "expected_value": (False, "YOU ENTERED GIBBERISH, TRY AGAIN! >:-("),
            },
            {
                "name": "user entered gibberish, numbers",
                "player_input": "123",
                "expected_value": (False, "YOU ENTERED GIBBERISH, TRY AGAIN! >:-("),
            },
            {
                "name": "r was entered and should be correct",
                "player_input": "r",
                "expected_value": (True, ""),
            },
            {
                "name": "rock was entered and should be correct",
                "player_input": "rock",
                "expected_value": (True, ""),
            },
        ]

        for case in testcases:
            the_value_returned = is_input_valid(case["player_input"])
            try:
                # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertTupleEqual
                self.assertTupleEqual(the_value_returned, case["expected_value"])
                print("test case: " + case["name"] + " ✅ passed")
            except Exception as e:
                print("test case: " + case["name"] + " ❌ failed" + ": " + str(e))

    def test_compare_input(self):
        testcases = [
            {
                "name": "both players input rock, should be a tie",
                "player1_input": "r",
                "player2_input": "rock",
                "expected_value": "It's a tie, play again! :-)",
            },
            {
                "name": "both players input paper, should be a tie",
                "player1_input": "paper",
                "player2_input": "paper",
                "expected_value": "It's a tie, play again! :-)",
            },
            {
                "name": "both players input scissors, should be a tie",
                "player1_input": "scissors",
                "player2_input": "s",
                "expected_value": "It's a tie, play again! :-)",
            },
            {
                "name": "player 1 wins, rock beats scissors",
                "player1_input": "rock",
                "player2_input": "scissors",
                "expected_value": "Player 1 wins!",
            },
            {
                "name": "player 1 wins, paper beats rock",
                "player1_input": "paper",
                "player2_input": "rock",
                "expected_value": "Player 1 wins!",
            },
            {
                "name": "player 1 wins, scissors beats paper",
                "player1_input": "scissors",
                "player2_input": "paper",
                "expected_value": "Player 1 wins!",
            },
            {
                "name": "player 1 losses, paper beats rock",
                "player1_input": "rock",
                "player2_input": "paper",
                "expected_value": "Player 2 wins!",
            },
            {
                "name": "player 1 losses, scissors beats paper",
                "player1_input": "paper",
                "player2_input": "scissors",
                "expected_value": "Player 2 wins!",
            },
            {
                "name": "player 1 losses, rock beats scissors",
                "player1_input": "scissors",
                "player2_input": "rock",
                "expected_value": "Player 2 wins!",
            },
        ]

        for case in testcases:
            the_value_returned = compare_input(
                case["player1_input"], case["player2_input"]
            )
            try:
                # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual
                self.assertEqual(the_value_returned, case["expected_value"])
                print("test case: " + case["name"] + " ✅ passed")
            except Exception as e:
                print("test case: " + case["name"] + " ❌ failed" + ": " + str(e))


if __name__ == "__main__":
    unittest.main()
