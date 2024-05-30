"""
Write a function called find_factors which accepts a number and returns a list of all of the numbers which it is
divisible by starting from 1 and going up to the number
- Ex:
    find_factors(10)  # [1, 2, 5, 10]
    find_factors(11)  # [1, 11]
    find_factors(111)  # [1, 3, 37, 111]
    find_factors(321421)  # [1, 293, 1097, 321421]
    find_factors(412146)  # [1, 2, 3, 6, 7, 9, 14, 18, 21, 42, 63, 126, 3271, 6542, 9813, 19626, 22897, 29439, 45794,
    58878, 68691, 137382, 206073, 412146]
"""


def find_factors(number: int) -> list[int]:
    factors_list = [num for num in range(1, number) if number % num == 0]
    factors_list.append(number)
    return factors_list


if __name__ == "__main__":
    print(find_factors(10))
    print(find_factors(11))
    print(find_factors(111))
    print(find_factors(321421))
    print(find_factors(412146))
