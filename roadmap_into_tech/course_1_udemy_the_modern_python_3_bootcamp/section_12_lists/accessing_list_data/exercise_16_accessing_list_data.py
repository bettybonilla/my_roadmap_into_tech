"""
I'm having a party and made a list of people I want to invite. Unfortunately,
I'm a terrible friend and made a couple of spelling errors. Please help me
correct them!
- Change "Hanna" to "Hannah"
- Change "Geoffrey" to "Jeffrey"
- Change "aparna" to "Aparna"
- Hint: You can use the following syntax to change a value of an existing list
element at the specific index: lst[0] = "NewValue"
    - Here, lst would represent the variable holding the list that we are
    modifying and the 0 in square brackets [] would be the index number of the
    targeted list element that we are changing. In addition, we would use the
    = assignment operator to set it to a new value.
    - You can use this approach with the people list in this exercise to make
    the necessary modifications as instructed above!
"""

# NO TOUCHING =================================================================
people = ["Hanna", "Louisa", "Claudia", "Angela", "Geoffrey", "aparna"]
# NO TOUCHING =================================================================

# Change "Hanna" to "Hannah"
people[0] = "Hannah"
print(people[0])

# Change "Geoffrey" to "Jeffrey"
people[4] = "Jeffrey"
print(people[4])
# Alternative code to access the second to last element in the list using
# negative indexing
# people[-2] = "Jeffrey"
# print(people[-2])

# Change "aparna" to "Aparna"
people[-1] = "Aparna"
print(people[-1])
# Alternative code to access the last element in the list using the
# len() function
# people[len(people) - 1] = "Aparna"
# print(people[len(people) - 1])
