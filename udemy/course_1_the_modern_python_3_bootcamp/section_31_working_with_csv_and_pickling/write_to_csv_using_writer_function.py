"""
The below shows how we can write to CSV files using the writer() function in the csv module
"""

import csv

with open("cats.csv", "w") as file:
    # You can create a writer object for writing to CSV files using the writer() function and pass in the CSV file
    csv_writer = csv.writer(file)
    # Then you can use the .writerow() method on the writer object to write a row to the CSV file by passing in a list
    csv_writer.writerow(["Name", "Age"])
    csv_writer.writerow(["Blue", 3])
    csv_writer.writerow(["Garfield", 10])
