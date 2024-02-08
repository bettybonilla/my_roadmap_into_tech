from typing import Callable, Optional, NoReturn


def do_work(data: int, callback: Optional[Callable[[int, ...], NoReturn]] = None):
    result = data * 2
    if callback:
        callback(result)
    return result


def do_work_ignore_result(data: int, callback: Optional[Callable[[], NoReturn]] = None):
    result = data * 2
    if callback:
        callback()
    return result


if __name__ == "__main__":

    def callback(result):
        print(f"the result is {result}")

    def callback2():
        print("work was done, hurrah!")

    do_work(2, callback)
    do_work_ignore_result(2, callback2)
    do_work(
        2,
        lambda result: print(f"the result is {result}")
        if result > 5
        else print("result is too low"),
    )
