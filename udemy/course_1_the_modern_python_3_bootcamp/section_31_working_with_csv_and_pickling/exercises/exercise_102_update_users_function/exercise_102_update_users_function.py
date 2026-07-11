"""
- For this exercise, you'll be working with a file called users.csv
- Each row of data consists of two columns: A user's first name and a user's last name
- Implement the following function:
    - update_users
        - Takes in an old first name, an old last name, a new first name, and a new last name
        - Updates the users.csv file so that any user whose first and last names match the old first and last names are
        updated to the new first and last names
        - The function should return a count of how many users were updated
- Ex:
    update_users("Grace", "Hopper", "Hello", "World")  # Users updated: 1.
    update_users("Colt", "Steele", "Boba", "Fett")  # Users updated: 2.
    update_users("Not", "Here", "Still not", "Here")  # Users updated: 0.
"""

import csv


def update_users(
    old_first_name: str, old_last_name: str, new_first_name: str, new_last_name: str
) -> str:
    with open("users.csv", "r+") as file:
        csv_reader = csv.reader(file)
        original_csv_data = list(csv_reader)
        # print(original_csv_data)

        old_name = [old_first_name, old_last_name]
        new_name = [new_first_name, new_last_name]

        updated_csv_data = original_csv_data
        updated_users_count = 0
        while old_name in updated_csv_data:
            old_name_index = updated_csv_data.index(old_name)
            updated_csv_data[old_name_index] = new_name
            updated_users_count += 1

        # print(updated_csv_data)
        # print(updated_users_count)

        file.seek(0)
        csv_writer = csv.writer(file)

        for row_list in updated_csv_data:
            csv_writer.writerow(row_list)

        file.truncate()
        return f"Users updated: {updated_users_count}."


# Alternative code
# def update_users(
#     old_first_name: str, old_last_name: str, new_first_name: str, new_last_name: str
# ) -> str:
#     with open("users.csv") as file:
#         csv_reader = csv.reader(file)
#         csv_data = list(csv_reader)
#
#     with open("users.csv", "w") as file:
#         csv_writer = csv.writer(file)
#
#         users_updated_count = 0
#         for row_list in csv_data:
#             if row_list[0] == old_first_name and row_list[1] == old_last_name:
#                 csv_writer.writerow([new_first_name, new_last_name])
#                 users_updated_count += 1
#             else:
#                 csv_writer.writerow(row_list)
#         return f"Users updated: {users_updated_count}."


if __name__ == "__main__":
    print(update_users("Grace", "Hopper", "Hello", "World"))
    print(update_users("Colt", "Steele", "Boba", "Fett"))
    print(update_users("Not", "Here", "Still not", "Here"))
