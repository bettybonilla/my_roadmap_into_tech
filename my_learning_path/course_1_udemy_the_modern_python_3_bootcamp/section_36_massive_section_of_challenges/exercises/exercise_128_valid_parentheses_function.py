"""
Write a function called valid_parentheses that takes a string of parentheses and determines if the order of the
parentheses is valid
- valid_parentheses should return True if the string is valid and False if it's invalid
- Ex:
    valid_parentheses("()")  # True
    valid_parentheses(")(()))")  # False
    valid_parentheses("(")  # False
    valid_parentheses("(())((()())())")  # True
    valid_parentheses('))((')  # False
    valid_parentheses('())(')  # False
    valid_parentheses('()()()()())()(')  # False
"""


def valid_parentheses(string: str) -> bool:
    if string[0] == "(" and string[-1] == ")":
        return True
    return False


if __name__ == "__main__":
    print(valid_parentheses("()"))
    print(valid_parentheses(")(()))"))
    print(valid_parentheses("("))
    print(valid_parentheses("(())((()())())"))
    print(valid_parentheses("))(("))
    print(valid_parentheses("())("))
    print(valid_parentheses("()()()()())()("))
