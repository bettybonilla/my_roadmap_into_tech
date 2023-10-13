"""
Since we downloaded and installed the termcolor package, we can now use it in
our code by importing it into our files
- NOTE: Some termcolor properties such as "blink" and others do not work in
VS Code or iTerm and only work in the actual Mac terminal
"""

from termcolor import colored

# The help() function is a built-in Python function that shows documentation
# for whatever we pass in to it
# In order to view the documentation conveniently while you code, open a
# separate terminal window and go into the terminal Python interpreter then
# import the package by using import package_name then you can run the
# help() function
# To exit this view, press q
# help(termcolor)

text = colored("Hi there!", "red")
print(text)
text = colored("Hi there!", "cyan")
print(text)

# Remember you can also use keyword arguments in your function call which
# makes your function call more readable and explicit
text = colored("Hi there!", color="yellow", on_color="on_magenta")
print(text)
text = colored("Hi there!", color="magenta", on_color="on_yellow")
print(text)
text = colored("Hi there!", color="magenta", on_color="on_yellow", attrs=["bold"])
print(text)
