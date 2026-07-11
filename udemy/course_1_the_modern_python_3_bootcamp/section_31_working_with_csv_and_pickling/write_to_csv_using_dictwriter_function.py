"""
The below shows how we can write to CSV files using the DictWriter() function in the csv module
"""

import csv

with open("cats.csv", "w") as file:
    # First you have to define your headers in a list or a tuple
    headers = ["Name", "Age"]
    # Then you can create a DictWriter object for writing to CSV files using the DictWriter() function and pass in the
    # CSV file and the fieldnames keyword argument which you assign to your headers
    csv_DictWriter = csv.DictWriter(file, fieldnames=headers)
    # Then you can use the .writeheader() method on the DictWriter object to write the header row to the CSV file which
    # uses the fieldnames keyword argument (you don't need to pass it in)
    csv_DictWriter.writeheader()
    # Then finally you can use the .writerow() method on the DictWriter object to write a row to the CSV file by passing
    # in a dictionary
    csv_DictWriter.writerow({"Name": "Blue", "Age": 3})
    csv_DictWriter.writerow({"Name": "Garfield", "Age": 10})
