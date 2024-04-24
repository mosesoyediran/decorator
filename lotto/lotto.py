import random


def repeat(num_times):
    """
    A decorator to repeat a function a specified number of times and return sorted results.

    This decorator takes a parameter indicating how many times to repeat the wrapped function. It then returns a list of the results of each function call, sorted in ascending order.

    Args:
        num_times (int): The number of times to repeat the function.

    Returns:
        callable: A wrapped function that, when called, repeats the original function `num_times` times and returns the sorted results.
    """
    def decorator(func):
        def inner(*args, **kwargs):
            result = []
            for _ in range(num_times):
                # Call the wrapped function and collect the result
                number = func(*args, **kwargs)
                result.append(number)
            return sorted(result)  # Return the sorted results
        return inner
    return decorator


@repeat(num_times=7)
def lotto_draw(start, end):
    """
    A function to draw a random number within a specified range.

    This function generates a random integer between `start` and `end`. It is decorated with `repeat`, so it draws a specified number of random numbers and returns them in sorted order.

    Args:
        start (int): The start of the range for the random draw.
        end (int): The end of the range for the random draw.

    Returns:
        list of int: A list of random numbers drawn from the specified range, sorted in ascending order.
    """
    return random.randint(start, end)
