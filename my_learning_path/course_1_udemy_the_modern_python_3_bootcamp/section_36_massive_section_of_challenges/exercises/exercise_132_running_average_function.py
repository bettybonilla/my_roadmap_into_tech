"""
- Create a function called running_average that returns a function
    - When the function returned is passed a value, the function returns the current average of all previous function
    calls - You will have to use closure to solve this
    - You should round all answers to the 2nd decimal place
- Ex:
    rAvg = running_average()
    rAvg(10)  # 10.0
    rAvg(11)  # 10.5
    rAvg(12)  # 11.0

    rAvg2 = running_average()
    rAvg2(1)  # 1.0
    rAvg2(3)  # 2.0
"""

from typing import Callable


def running_average(x: float = 0.0) -> Callable[[int], float]:
    num = x

    def inner(y: int) -> float:
        y = float(y)
        nonlocal num
        if num == 0.0:
            num = y
            return num
        return (num + y) / 2.0

    return inner


# Alternative code
# def running_average() -> Callable[[int], float]:
#     running_average.accumulator = 0
#     running_average.size = 0
#
#     def inner(number: int) -> float:
#         running_average.accumulator += number
#         running_average.size += 1
#         return running_average.accumulator / running_average.size
#
#     return inner


if __name__ == "__main__":
    rAvg = running_average()
    print(rAvg(10))
    print(rAvg(11))
    print(rAvg(12))

    rAvg2 = running_average()
    print(rAvg2(1))
    print(rAvg2(3))
