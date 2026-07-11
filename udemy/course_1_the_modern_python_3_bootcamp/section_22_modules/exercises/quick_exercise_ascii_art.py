"""
Install the pyfiglet package and write a program to print colored text art
- Use the termcolor package in order to provide a color to the text art
- Set a default color of your choosing in case a color is not provided in the
input or found in the termcolor package
- NOTE: Don't over-engineer it ! ! !
"""

from pyfiglet import figlet_format
from termcolor import colored

VALID_TERMCOLOR_COLORS = (
    "black",
    "red",
    "green",
    "yellow",
    "blue",
    "magenta",
    "cyan",
    "white",
    "light_grey",
    "dark_grey",
    "light_red",
    "light_green",
    "light_yellow",
    "light_blue",
    "light_magenta",
    "light_cyan",
)

message = input("What message do you want to print?: ")
color = input("What color?: ")

if color not in VALID_TERMCOLOR_COLORS:
    color = "yellow"

if message:
    figlet_text_art = figlet_format(message)
    colored_figlet_text_art = colored(figlet_text_art, color=color)
print(colored_figlet_text_art)
