"""
- For this exercise, you'll be working with a file called users.csv
- Each row of data consists of two columns: A user's first name and a user's last name
- Implement the following function:
    - add_user
        - Takes in a first name and a last name and adds a new user to the users.csv file
- Ex:
    add_user("Dwayne", "Johnson")  # None

    # users.csv now has two data rows:
    # First Name,Last Name
    # Colt,Steele
    # Dwayne,Johnson
"""

import csv


def add_user(first_name: str, last_name: str):
    with open("users.csv", "a") as file:
        csv_writer_file = csv.writer(file)
        csv_writer_file.writerow([first_name, last_name])


if __name__ == "__main__":
    add_user("Dwayne", "Johnson")
