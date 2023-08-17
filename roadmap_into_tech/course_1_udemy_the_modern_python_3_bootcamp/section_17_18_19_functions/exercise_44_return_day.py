"""
Write a function called return_day
- This function takes in one parameter (a number from 1-7) and returns the day
of the week (1 is Sunday, 2 is Monday, 3 is Tuesday, etc.)
- If the number is less than 1 or greater than 7, the function should return
None
- Hint: Store the days of the week in a list or a dict using the numbers as
keys
"""


def return_day(num: int) -> str:
    days_of_week = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday",
    }

    return days_of_week.get(num)


print(return_day(1))
print(return_day(2))
print(return_day(3))
print(return_day(4))
print(return_day(5))
print(return_day(6))
print(return_day(7))
print(return_day(0))
print(return_day(8))
print(return_day(41))
