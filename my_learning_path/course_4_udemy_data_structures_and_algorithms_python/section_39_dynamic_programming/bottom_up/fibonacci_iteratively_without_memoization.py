"""
The below shows how to use dynamic programming iteratively without memoization to calculate the Fibonacci sequence of a
number
"""

func_call_counter = 0


def fib(num: int) -> int:
    global func_call_counter
    fib_list = [0, 1]
    for i in range(2, n + 1):
        func_call_counter += 1
        next_fib = fib_list[i - 1] + fib_list[i - 2]
        fib_list.append(next_fib)
    print(fib_list)
    return fib_list[num]


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
