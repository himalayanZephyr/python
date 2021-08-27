import time
from functools import wraps

def slow_down(sleep_time):
    
    def func_wrapper(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Slowing down function '{func.__name__}' by {sleep_time} sec")
            time.sleep(sleep_time)
            return func(*args, **kwargs)
        return wrapper

    return func_wrapper

@slow_down(sleep_time=2)
def print_hello():
    print("Hello")

@slow_down(sleep_time=4)
def print_hi():
    print("Hi")


if __name__ == "__main__":
    print_hello()
    print_hi()

    print("Printing Function Names: ")
    print(print_hello.__name__)
    print(print_hi.__name__)
