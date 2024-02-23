"""
- For this exercise, you'll be working with a file called users.csv
- Each row of data consists of two columns: A user's first name and a user's last name
- Implement the following function:
    - print_users
        - Prints out all the first and last names in the users.csv file
- Ex:
    print_users()  # None

    # prints to the console:
    # Colt Steele
"""

import csv


def print_users():
    with open("users.csv") as file:
        csv_reader = csv.reader(file)

        next(csv_reader)
        for row_list in csv_reader:
            print(f"{row_list[0]} {row_list[1]}")


if __name__ == "__main__":
    print_users()
