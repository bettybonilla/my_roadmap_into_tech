"""
The below shows how we can use the DictReader() function and the DictWriter() function in the csv module to read to a
CSV file, convert data from cm to in, then write the converted data to a non-existing CSV file which gets newly created
for you
"""

import csv
from typing import Any


def cm_to_in(cm: Any) -> float:
    # The cm argument that is being passed in from the csv_dictreader_file is a string therefore we have to convert it
    # to a float - This way any data type that is passed in will be converted properly before it's used
    inches = float(cm) * 0.393701
    inches_rounded = round(inches, 2)
    return inches_rounded


with open("street_fighter_fighters.csv") as file:
    csv_dictreader_file = csv.DictReader(file)
    data = list(csv_dictreader_file)

with open("street_fighter_fighters_height_in_inches.csv", "w") as file:
    headers = ["Name", "Country", "Height (in inches)"]
    csv_dictwriter_file = csv.DictWriter(file, fieldnames=headers)
    csv_dictwriter_file.writeheader()

    for fighter in data:
        csv_dictwriter_file.writerow(
            {
                "Name": fighter["Name"],
                "Country": fighter["Country"],
                "Height (in inches)": cm_to_in(fighter["Height (in cm)"]),
            }
        )
