cache_count_dictonary = dict()
write_count_dictonary = dict()

cache_file = open("cache.csv", "r")
for row in cache_file.readlines()[1:]: # https://stackoverflow.com/questions/509211/understanding-slice-notation
	publisher_name, count  = row.split(",")
	cache_count_dictonary[publisher_name] = float(count)
cache_file.close()

write_file = open("write.csv", "r")
for row in write_file.readlines()[1:]:
	publisher_name, count  = row.split(",")
	write_count_dictonary[publisher_name] = float(count)
write_file.close()


# the keys for both dictionarys will be the same, so i can use the key from 1 dictionary as the lookup key for the other dictionary
for publisher_name, cache_value in cache_count_dictonary.items():
	try:
		write_value = write_count_dictonary[publisher_name]
		rate = (1 - (int(write_value) / int(cache_value))) * 100
		print(f"Publisher: {publisher_name} -> LossRate: {rate}.")
	except KeyError as e:
		print(f"the publisher_name {publisher_name} was missing from the write_file")	# https://realpython.com/python-f-strings/
