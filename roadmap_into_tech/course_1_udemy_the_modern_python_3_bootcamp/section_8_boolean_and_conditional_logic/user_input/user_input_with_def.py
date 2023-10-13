"""
The below shows another way you can get user input by using a def (definition)
which defines a function so you can reuse it again throughout your code
"""

# -----------------------------------------------------------------------------
# TODO Step 1: Revisit and test knowledge once conditional programming courses
# are completed
# TODO Step 2: Revisit and test knowledge once definition programming courses
# are completed
# -----------------------------------------------------------------------------


# Using a def implements the DRY (Don't Repeat Yourself) principle because you
# define your function once and then you can reuse it without having to repeat
# the same code for it again
# The 1st line is your signature line where you use a clear name (green) to
# describe what your function will do then you write your parameters inside
# the parentheses
# The rest of the def code block follows each line of code in order
def get_user_input(question):
    print(question)
    user_answer = input().lower().strip()
    # print(f"you said {user_answer}")
    return user_answer


data1 = get_user_input("What's your 1st favorite color?")
data2 = get_user_input("What's your 2nd favorite color?")

# The pass keyword leaves a placeholder for your code so that you can come
# back to it later without having to finish the indented code otherwise,
# Python will mark it as a problem
if data1 == "red":
    # do something
    pass
