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
    csv_DictReader = csv.DictReader(file)
    csv_data = list(csv_DictReader)

with open("street_fighter_fighters_height_in_inches.csv", "w") as file:
    headers = ["Name", "Country", "Height (in inches)"]
    csv_DictWriter = csv.DictWriter(file, fieldnames=headers)
    csv_DictWriter.writeheader()

    for row_OrderedDict in csv_data:
        csv_DictWriter.writerow(
            {
                "Name": row_OrderedDict["Name"],
                "Country": row_OrderedDict["Country"],
                "Height (in inches)": cm_to_in(row_OrderedDict["Height (in cm)"]),
            }
        )
