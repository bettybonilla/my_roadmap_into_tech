"""
- Write a function called week which returns a generator that yields each day of the week, starting with Monday and
ending with Sunday
- After Sunday, the generator is exhausted - It does not start over
    - Ex:
        days = week()
        next(days)  # 'Monday'
        next(days)  # 'Tuesday'
        next(days)  # 'Wednesday'
        next(days)  # 'Thursday'
        next(days)  # 'Friday'
        next(days)  # 'Saturday'
        next(days)  # 'Sunday'
        next(days)  # StopIteration
"""

from typing import Iterator


def week() -> Iterator[str]:
    days_in_week = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]

    for day in days_in_week:
        yield day


days = week()
print(next(days))
print(next(days))
print(next(days))
print(next(days))
print(next(days))
print(next(days))
print(next(days))
print(next(days))
