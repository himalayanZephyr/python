import time
from functools import wraps

def timeit(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        results = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time elapsed for {func.__name__} : { end_time - start_time}")
        return results

    return wrapper


@timeit
def square(nums):
    squared_nums = []
    for num in nums:
        squared_nums.append(num*num)

    return squared_nums

@timeit
def cube(nums):
    cubed_nums = []
    for num in nums:
        cubed_nums.append(num*num*num)

    return cubed_nums


if __name__ == "__main__":
    nums = range(1,100)

    print(square(nums))
    print("="*50)
    print(cube(nums))
    print("="*50)
    print("Function names :")
    print(square.__name__)
    print(cube.__name__)
