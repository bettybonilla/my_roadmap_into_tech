import unittest
from typing import Any, Dict

from fizz_buzz import fizz_buzz, fizz_buzz_str, adder


class Case:
    def __init__(self, name: str, expected: Any, **kwargs: Dict[str, Any]):
        self.name = name
        self.expected = expected
        self.arguments = kwargs


class Test(unittest.TestCase):
    def test_fizz_buzz(self):
        cases = [
            Case("should return fizzbuzz", "FizzBuzz", n=15),
            Case("should return fizz", "Fizz", n=3),
            Case("should return buzz", "Buzz", n=5),
        ]

        for c in cases:
            print(f"Test case: {c.name}")
            self.assertEqual(c.expected, fizz_buzz(c.arguments["n"]), msg=c.name)

    def test_fizz_buzz_str(self):
        cases = [
            Case("should return 0", 0, s="FizzBuzz"),
            Case("should return 1", 1, s="Fizz"),
            Case("should return 2", 2, s="Buzz"),
        ]

        for c in cases:
            print(f"Test case: {c.name}")
            self.assertEqual(c.expected, fizz_buzz_str(c.arguments["s"]), msg=c.name)

    def test_adder(self):
        cases = [
            Case("should return 3", 3, a=1, b=2),
            Case("should return 5", 5, a=2, b=3),
            Case("should return 7", 7, a=3, b=4),
        ]

        for c in cases:
            print(f"Test case: {c.name}")
            self.assertEqual(
                c.expected, adder(c.arguments["a"], c.arguments["b"]), msg=c.name
            )


if __name__ == "__main__":
    unittest.main()
