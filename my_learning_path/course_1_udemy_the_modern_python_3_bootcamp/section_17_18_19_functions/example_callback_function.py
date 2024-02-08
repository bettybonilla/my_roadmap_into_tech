from typing import Callable, Optional


def do_work(data: int, callback: Optional[Callable] = None):
    result = data * 2
    if callback:
        callback(result)
    return result


if __name__ == "__main__":

    def callback(result):
        print(f"the result is {result}")

    do_work(2, callback)
