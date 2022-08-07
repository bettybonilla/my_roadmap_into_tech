import argparse
import csv
import json
import sys

# allows me to pass in data from the command line as variables, rather than hardcoding them, it makes the script more reuseable
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', help="APS CSV")
parser.add_argument('-j', '--json', help="APS JSON FROM DB")
args = parser.parse_args()

if not args.json:
    print("database json required")
    sys.exit(0)

if args.file:
    with open(args.file, 'r') as cin:
        # new Slot Name     cpm     Price Points    Encoded Price Points    Slot Size
        reader = csv.DictReader(cin)
        # clean up the CSV, if the file was opened in excel there will be bad data in the files binary
        reader.fieldnames = [i.strip().replace("\ufeff", "") for i in reader.fieldnames]

        # load in the JSON data from the file python
        json_file = open(args.json, 'r')
        nimbus_map = json.loads(json_file.read())
        json_file.close() # don't forget to close the file since I'm not using the with statement

        #create a counter variable so that is an exception occurs, I know which line number the bad data exist in
        counter = 1
        for row in reader:
            # make the key lower case so that the script doesn't break if some of the values are uppercased
            key_slot_size = row["Slot Size"].lower()
            slot_name = row["Slot Name"].lower()

            # normalize amazon naming to match nimbus naming
            if (key_slot_size == "interstitial" or key_slot_size == "640x390") and slot_name.find("video") > -1:
                key_slot_size = "video"
            elif key_slot_size == "interstitial":
                key_slot_size = "320x480"

            try:
                kv = row["Price Points"]
                cpm = row["cpm"]
                if key_slot_size in nimbus_map:
                    if kv in nimbus_map[key_slot_size]:
                        print("there was a duplicate key on line " + str(counter))
                        sys.exit(1)

                #update the map by adding the new unique key
                nimbus_map[key_slot_size][kv] = float(cpm)
                counter += 1
            except Exception as ex:
                template = "CSV ROW #{0}, An exception of type {1} occurred. Arguments:\n{2!r}"
                message = template.format(counter, type(ex).__name__, ex.args)
                print(message)
                sys.exit(1)

    # print out the data so that it can be copied into the database as JSON
    print(nimbus_map)