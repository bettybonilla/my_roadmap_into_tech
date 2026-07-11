"""
The below shows the inefficiency of using recursion without memoization to calculate the Fibonacci sequence of a number
"""

func_call_counter = 0


def fib(num: int) -> int:
    global func_call_counter
    func_call_counter += 1

    # print(f"We are at: {num}")
    # Base case (exit condition)
    if num == 0 or num == 1:
        return num
    # Recursive case
    else:
        return fib(num - 1) + fib(num - 2)


if __name__ == "__main__":
    n = 4
    print(f"Fibonacci of {n} =", fib(n))
    print(f"Function calls made on call stack: {func_call_counter:,}")
    print("")

    n = 10
    print(f"Fibonacci of {n} =", fib(n))
    print(f"Function calls made on call stack: {func_call_counter:,}")
    print("")

    n = 20
    print(f"Fibonacci of {n} =", fib(n))
    print(f"Function calls made on call stack: {func_call_counter:,}")
    print("")

    n = 35
    print(f"Fibonacci of {n} =", fib(n))
    print(f"Function calls made on call stack: {func_call_counter:,}")
