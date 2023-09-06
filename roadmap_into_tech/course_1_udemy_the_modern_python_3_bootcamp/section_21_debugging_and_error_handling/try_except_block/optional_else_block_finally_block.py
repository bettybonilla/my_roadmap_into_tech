"""
The below shows how you can use the optional else block and finally block with
a try/except block in a while loop
"""

# Prints the reciprocal of even numbers only
while True:
    try:
        num = int(input("Enter an even number: "))
        # The assert keyword acts as a sanity check to ensure that certain
        # conditions are met during the execution of a program - However, it
        # should only be used for testing and debugging, not in production
        # environments
        # If the expression returns True, the program moves to the next line
        # however if the expression returns False, an AssertionError is
        # generated
        assert num % 2 == 0
    # As mentioned, you can have multiple except blocks in a try/except block
    # so that you can error catch/handle each exception/error differently
    except ValueError:
        print("Error: that's not a number!")
    except AssertionError:
        print("Error: that's not an even number!")
    else:
        reciprocal = 1 / num
        print(reciprocal)
        break
    finally:
        print("Runs no matter if an exception/error occurs or not")

print("Rest of program logic executes!")
