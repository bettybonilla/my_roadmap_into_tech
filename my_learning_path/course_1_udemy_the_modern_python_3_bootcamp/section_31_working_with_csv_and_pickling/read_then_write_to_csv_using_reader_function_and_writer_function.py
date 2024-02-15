"""
The below shows how we can use the reader() function and the writer() function in the csv module to read to a CSV file,
uppercase the data, then write the uppercased data to a non-existing CSV file which gets newly created for you
"""

import csv

with open("street_fighter_fighters.csv") as file:
    csv_reader_file = csv.reader(file)

    # We need to use a nested list comprehension since, when we iterate using a list comprehension in for row in
    # csv_reader_file, it gets converted to a list of nested lists so that's why the nested list comprehension is needed
    data_uppercased = [[data.upper() for data in row] for row in csv_reader_file]

    # Checks that the data was uppercased
    # for row in data_uppercased:
    #     print(row)

with open("street_fighter_fighters_uppercased.csv", "w") as file:
    csv_writer_file = csv.writer(file)

    # However you can only loop over an iterator once before it gets exhausted so the previous for loop is commented out
    for row in data_uppercased:
        csv_writer_file.writerow(row)

# Alternative code using nested with statements
# You must use a nested with statement since a nested with statement would prevent the first with statement from closing
# and preventing access to this CSV file since otherwise this file would be automatically closed for you
# It's bad practice to keep more than one file opened at a time however if you're just transferring altered data from
# one file to another file, it's not too much of a problem
# with open("street_fighter_fighters.csv") as file:
#     csv_reader_file = csv.reader(file)
#
#     with open("street_fighter_fighters_uppercased.csv", "w") as file:
#         csv_writer_file = csv.writer(file)
#         for row in csv_reader_file:
#             csv_writer_file.writerow([data.upper() for data in row])
