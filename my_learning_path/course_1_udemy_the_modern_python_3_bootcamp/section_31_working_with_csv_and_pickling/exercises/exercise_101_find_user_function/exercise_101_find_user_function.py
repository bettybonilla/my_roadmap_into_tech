"""
- For this exercise, you'll be working with a file called users.csv
- Each row of data consists of two columns: A user's first name and a user's last name
- Implement the following function:
    - find_user
        - Takes in a first name and a last name and searches for a user with that first and last name in the users.csv
        file
        - If the user is found, find_user returns the index where the user is found
        - Otherwise, it returns a message stating that the user wasn't found
- Ex:
    find_user("Colt", "Steele")  # 1
    find_user("Alan", "Turing")  # 3
    find_user("Not", "Here")  # 'Not Here not found.'
"""

import csv


def find_user(first_name: str, last_name: str) -> int | str:
    with open("users.csv") as file:
        csv_reader = csv.reader(file)
        csv_data = list(csv_reader)

        for row_list in csv_data:
            if row_list[0] == first_name and row_list[1] == last_name:
                return csv_data.index(row_list)
        return f"{first_name} {last_name} not found."


if __name__ == "__main__":
    print(find_user("Colt", "Steele"))
    print(find_user("Alan", "Turing"))
    print(find_user("Not", "Here"))
