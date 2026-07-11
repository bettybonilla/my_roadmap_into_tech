"""
- For this exercise, you'll be working with a file called users.csv
- Each row of data consists of two columns: A user's first name and a user's last name
- Implement the following function:
    - delete_users
        - Takes in a first name and a last name
        - Updates the users.csv file so that any user whose first and last names match the inputs are removed
        - The function should return a count of how many users were removed
- Ex:
    delete_users("Grace", "Hopper")  # Users deleted: 1.
    delete_users("Colt", "Steele")  # Users deleted: 2.
    delete_users("Not", "Here")  # Users deleted: 0.
"""

import csv


def delete_users(first_name: str, last_name: str) -> str:
    with open("users.csv", "r+") as file:
        csv_reader = csv.reader(file)
        csv_data = list(csv_reader)

        user_deleted_count = 0
        for row_list in csv_data:
            # Alternative code
            # if row_list[0] == first_name and row_list[1] == last_name:
            if first_name and last_name in row_list:
                csv_data.remove(row_list)
                user_deleted_count += 1

        file.seek(0)
        csv_writer = csv.writer(file)

        for row_list in csv_data:
            csv_writer.writerow(row_list)

        file.truncate()
        return f"Users deleted: {user_deleted_count}."


# Alternative code
# def delete_users(first_name: str, last_name: str) -> str:
#     with open("users.csv") as file:
#         csv_reader = csv.reader(file)
#         csv_data = list(csv_reader)
#
#     with open("users.csv", "w") as file:
#         csv_writer = csv.writer(file)
#
#         user_deleted_count = 0
#         for row_list in csv_data:
#             # Alternative code
#             # if row_list[0] == first_name and row_list[1] == last_name:
#             if first_name and last_name in row_list:
#                 user_deleted_count += 1
#             else:
#                 csv_writer.writerow(row_list)
#         return f"Users deleted: {user_deleted_count}."


if __name__ == "__main__":
    print(delete_users("Grace", "Hopper"))
    print(delete_users("Colt", "Steele"))
    print(delete_users("Not", "Here"))
