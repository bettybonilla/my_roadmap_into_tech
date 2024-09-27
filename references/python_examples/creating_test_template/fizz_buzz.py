def fizz_buzz(n: int) -> str | int:
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n


def fizz_buzz_str(s: str) -> int:
    if s == "FizzBuzz":
        return 0
    elif s == "Fizz":
        return 1
    elif s == "Buzz":
        return 2
    else:
        return int(s)


def adder(a: int, b: int) -> int:
    return a + b
