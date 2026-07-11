"""
The below shows how we can read to CSV files using the DictReader() function in the csv module
"""

import csv

with open("street_fighter_fighters.csv") as file:
    csv_DictReader = csv.DictReader(file)
    # Returns a csv.DictReader object which is an iterator
    print(csv_DictReader)
    iterator = iter(csv_DictReader)
    # Matches the print statement above which shows that the csv.DictReader object is in fact an iterator
    print(iterator)
    print("")

    # When we iterate over the csv.DictReader object, each row in the CSV file will be represented as an OrderedDict
    # for row_OrderedDict in csv_DictReader:
    #     print(row_OrderedDict)

    # If you want to access specific values in the CSV file, you must reference their key (like a dictionary)
    # The keys are set up automatically to be the headers if headers were provided in the CSV file
    # Since the keys are the headers we don't have to worry about skipping them unlike when using the reader() function
    # Each row is an OrderedDict since the keys are always in the same order (Ex: Name, Country, Height (in cm))
    # However as previously mentioned, when we loop over the csv.DictReader object, since it is an iterator not an
    # iterable we have to comment out the previous for loop since we can only loop over an iterator once before it gets
    # exhausted
    # for row_OrderedDict in csv_DictReader:
    #     print(f"{row_OrderedDict['Name']} is from {row_OrderedDict['Country']}")

    # As previously mentioned, if you wanted to work with the data in the CSV file more than just once, you can convert
    # it to an iterable list since you can loop over iterables more than once
    csv_data = list(csv_DictReader)
    # This will print the csv_data as a list of nested OrderedDicts with each row in the CSV file being its own nested
    # OrderedDict inside the list
    # All row data inside each row OrderedDict in the csv_data is a string
    # csv_data: list[OrderedDict[str, str]] - Python bug does not accept that this is the correct type annotation
    # https://stackoverflow.com/questions/41207128/how-do-i-specify-ordereddict-k-v-types-for-mypy-type-annotation
    print(csv_data)
    print("")

    for row_OrderedDict in csv_data:
        print(row_OrderedDict)
    print("")

    for row_OrderedDict in csv_data:
        print(f"{row_OrderedDict['Name']} is from {row_OrderedDict['Country']}")
