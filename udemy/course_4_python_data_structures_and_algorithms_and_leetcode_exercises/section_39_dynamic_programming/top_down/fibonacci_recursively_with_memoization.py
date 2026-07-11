"""
The below shows the efficiency of using recursion with memoization to calculate the Fibonacci sequence of a number
"""

# Memoization implementation
# Stores up to the Fibonacci sequence of 99
memo = [None] * 100
func_call_counter = 0


def fib(num: int) -> int:
    global memo
    global func_call_counter
    func_call_counter += 1

    if memo[num] is not None:
        return memo[num]

    # print(f"We are at: {num}")
    # Base case (exit condition)
    if num == 0 or num == 1:
        return num
    # Recursive case
    else:
        memo[num] = fib(num - 1) + fib(num - 2)
        return memo[num]


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
    print("")

    n = 99
    print(f"Fibonacci of {n} =", fib(n))
    print(f"Function calls made on call stack: {func_call_counter:,}")
