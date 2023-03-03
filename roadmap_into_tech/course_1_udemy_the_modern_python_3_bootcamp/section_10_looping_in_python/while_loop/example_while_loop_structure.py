# basic while loop structure

# while True:
#     # do something
#     pass

# while False:
#     # do something
#     pass

# -------------------

# example 1: using boolean conditions
user_is_complete = False
total = 0
while not user_is_complete:
    # do some work e.g. run some calculations
    total += 10

    # if the desired condition is met, change the value of user_is_complete to
    # True which will stop the while loop
    if total == 200:
        user_is_complete = True

# example 2: using comparisons
retries = 0
data = None
while retries < 3:
    # do some complicated work like trying to get data from a website, in this
    # case I'll fake it
    # try changing retries == 3 and see if "got some data" is printed
    if retries == 2:
        data = "complete"

    if data == "complete":
        # the break statement exits the while loop immediately
        # this allows a programmer to exit once they have received what they
        # were waiting for rather than waiting for all the retries
        # also see the continue statement
        # https://www.tutorialspoint.com/python/python_continue_statement.htm
        break

    # incrementing retries that the while loop exits even if the request fails
    # on every retry
    retries += 1

if data:
    print("got some data")
