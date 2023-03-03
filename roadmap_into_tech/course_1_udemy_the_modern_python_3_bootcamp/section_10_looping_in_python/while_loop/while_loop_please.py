"""
Below is an example of a while loop
- When you run the program, user_input will be None so therefore while
user_input != "please": is True and will carry out the indented line of code
- The program will continue to carry out and run the indented line of code
user_input = input("Ah Ah Ah, you didn't say the magic word: ") until you
enter “please” because the while condition will remain True and will only end
until it is False by entering “please” which stops the execution of the loop
- NOTE: You MUST stop the program from running either by ending the while loop
or by using Ctrl + C to exit the program in terminal
"""

user_input = None

while user_input != "please":
    user_input = input("Ah Ah Ah, you didn't say the magic word: ")
