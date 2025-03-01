"""
Given: my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
- Create a  while  loop that prints all elements of the my_list variable 3 times
- When printing the elements, use a for loop to print the elements - However, if the element of the for loop is equal to
Monday, continue without printing
"""


# Solution 1
def repeating_days(list1: list[str]):
    index = 0
    while index < 5:
        for i in range(3):
            day = list1[index]
            if day == "Monday":
                continue
            print(day)
        index += 1


# Solution 2
def non_repeating_days(list1: list[str]):
    x = 0
    while x < 3:
        for i in list1:
            day = i
            if day == "Monday":
                continue
            print(day)
        x += 1


if __name__ == "__main__":
    my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    repeating_days(my_list)
    print("")
    non_repeating_days(my_list)
