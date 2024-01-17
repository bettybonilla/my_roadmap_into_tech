import json

# pass in the dictionary as a variable
def recusive_example_code(dictionary):
    # recursion is when a function calls itself, be aware of something called infinate recursion...
    # all recursions need to stop at some point, if they don't the program will crash with a stack overflow error
    for key, value in dictionary.items():
        # if the value i'm currently looking is also a dictionary, it means it's nested
        # so we want to pass in the sub dictionary into the function again
        if isinstance(value, dict):
            recusive_example_code(value)
        else:
            print(key, value)


# with is called a clousure statement and open is how you open files
# with is useful because it will automatically close the open file when your program doesn't need it anymore
# without with the code would look like this, note you have to close the file when you are done yourself
# json_file = open('example.json', 'r')
# your code....
# json_file.close()
with open("example.json", "r") as json_file:
    dictionary = json.load(json_file)
    # print all the keys
    print(dictionary.keys())
    print("--------")
    # print all the values
    print(dictionary.values())
    print("--------")
    # access a top level key
    print(dictionary["app"])
    print("--------")
    # access a nested key
    print(dictionary["app"]["bundle"])
    print("--------")

    # iterate or range over keys
    for key, value in dictionary.items():
        # this will only print top level keys and their values
        # to access inner keys, you may use something like recursion
        print(key, value)

    print("--------")
    print("--------")
    # example of how to print all the keys and values, the function recusive_example_code will "flatten"
    # the dictionary as if all the keys were top level
    recusive_example_code(dictionary)
