"""
This exercise requires two files ! ! !
- Your task is to write a function in the helpers.py file and then call it
from the exercise.py file - More specifically:
    - In the helpers.py file, define a function called lucky_number() that
    always returns the number 37 - That's it, it always returns 37 no matter
    what
    - In the exercise.py file, import the helpers module - In order for the
    testing logic to work properly, don't use the as or from keywords when
    importing
    - Then from inside the exercise.py file, call the lucky_number() function
    you defined in the helpers module and save the result to a variable called
    num
- NOTE: The point of this exercise is to get comfortable working with multiple
files and defining custom modules - Because of that, the testing logic
actually checks to see that your code is in all the correct files rather than
just checking if you got the right answer
"""

import helpers

num = helpers.lucky_number()
print(num)
