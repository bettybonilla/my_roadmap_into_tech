"""
The below shows how we can read to CSV files using the reader() function in the csv module
"""

import csv

with open("street_fighter_fighters.csv") as file:
    csv_reader = csv.reader(file)
    # Returns a csv.reader object which is an iterator
    print(csv_reader)
    iterator = iter(csv_reader)
    # Matches the print statement above which shows that the csv.reader object is in fact an iterator
    print(iterator)
    print("")

    # When we iterate over the csv.reader object, each row in the CSV file will be represented as a list
    # The first row list will be the headers if headers were provided in the CSV file
    # for row_list in csv_reader:
    #     print(row_list)

    # If you want to access specific values in the CSV file, you must reference their index
    # However when we loop over the csv.reader object, since it is an iterator not an iterable we have to comment out
    # the previous for loop since we can only loop over an iterator once before it gets exhausted
    # This is because the next() function is being called on the iterator until it reaches the end of the loop and, once
    # it's at the end, it then raises the StopIteration error which is being intercepted in the background
    # To skip the first row list with the headers, you can call the next() function on your CSV file before you start
    # your iteration
    # next(csv_reader)
    # for row_list in csv_reader:
    #     print(f"{row_list[0]} is from {row_list[1]}")

    # If you wanted to work with the data in the CSV file more than just once, you can convert it to an iterable list
    # since you can loop over iterables more than once
    csv_data = list(csv_reader)
    # This will print the csv_data as a list of nested lists with each row in the CSV file being its own nested list
    # inside the list
    # csv_data: list[list[str]]
    print(csv_data)
    print("")

    for row_list in csv_data:
        print(row_list)
    print("")

    for row_list in csv_data:
        # Skips the first row nested list with the headers inside the list
        if row_list == csv_data[0]:
            continue
        print(f"{row_list[0]} is from {row_list[1]}")
