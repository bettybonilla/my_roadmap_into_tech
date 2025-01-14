"""
The below shows how a call stack executes in code
"""


def func_one():
    func_two()
    print("One")


def func_two():
    func_three()
    print("Two")


def func_three():
    print("Three")


if __name__ == "__main__":
    # Add a breakpoint to the line below where you want to analyze your code then click on the Debug button and use the
    # ↓ Step Into arrow to see how the call stack gets updated in Threads & Variables vs. the output in Console
    func_one()
