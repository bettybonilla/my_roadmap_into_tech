import csv  # https://docs.python.org/3/library/csv.html

cache_count_dictonary = dict()
write_count_dictonary = dict()


# open both boths and store csv data as dictionary data
with open("cache.csv", "r") as cache_file:
    reader = csv.DictReader(cache_file)
    for row in reader:
        cache_count_dictonary[row["publisher"]] = row["count"]


with open("write.csv", "r") as write_file:
    reader = csv.DictReader(write_file)
    for row in reader:
        write_count_dictonary[row["publisher"]] = row["count"]


loss_rate = list()  # https://www.w3schools.com/python/python_lists.asp


# the keys for both dictionarys will be the same, so i can use the key from 1 dictionary as the lookup key for the other dictionary
for publisher_name, cache_value in cache_count_dictonary.items():
    try:
        write_value = write_count_dictonary[publisher_name]
        rate = (1 - (int(float(write_value)) / int(float(cache_value)))) * 100
        loss_rate.append(
            (publisher_name, rate)
        )  # https://www.w3schools.com/python/python_tuples.asp
    except KeyError as e:
        print(
            f"the publisher_name {publisher_name} was missing from the write_file"
        )  # https://realpython.com/python-f-strings/

# loop over all the stored data and print it
for item in loss_rate:
    (
        publisher_name,
        rate,
    ) = item  # https://www.w3schools.com/python/python_tuples_unpack.asp
    print(f"Publisher: {publisher_name} -> LossRate: {rate}.")
