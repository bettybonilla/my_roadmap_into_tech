# -----------------------------------------------------------------------------
# TODO Revisit and test knowledge
# -----------------------------------------------------------------------------

# my_list_of_fruits = ["apples", "pears", "grapes", "avocados"]

# # creates copies (local variables)
# for fruit in my_list_of_fruits:
#     print("copy of " + fruit)

# # access fruits directly
# for i in range(len(my_list_of_fruits)):
#     print("fruit item " + my_list_of_fruits[i])


my_list_of_fruits = ["apples", "pears", "grapes", "avocados"]

# creates copies (local variables)
for fruit in my_list_of_fruits:
    fruit = fruit + "modified"
    print("copy of " + fruit)

# creates copies (local variables)
for fruit in my_list_of_fruits:
    print("copy of 2 " + fruit)

# access fruits directly
for i in range(len(my_list_of_fruits)):
    my_list_of_fruits[i] = my_list_of_fruits[i] + " modified"
    print("fruit item " + my_list_of_fruits[i])

# access fruits directly
for i in range(len(my_list_of_fruits)):
    print("fruit item 2 " + my_list_of_fruits[i])

# https://stackoverflow.com/questions/988155/how-do-i-operate-on-the-actual-object-not-a-copy-in-a-python-for-loop
