import time


def timed(func):
    """
    A decorator to measure the execution time of a function.

    This decorator wraps a function, times its execution, and prints how long the function took to execute. It can be applied to any function and will display the function's name and execution time in seconds.

    Args:
        func (callable): The function to wrap and time.

    Returns:
        callable: A wrapped function that measures its execution time.
    """
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()  # Record the start time
        result = func(*args, **kwargs)  # Execute the function
        end_time = time.perf_counter()  # Record the end time

        # Calculate and print the elapsed time
        print(f"Function {func.__name__} took {round(end_time - start_time, 4)} seconds to execute.")
        return result  # Return the result of the original function

    return wrapper


@timed
def loop_this_many_times(n=10**6):
    """
    A function that loops a specified number of times.

    This function does nothing but loop `n` times, primarily used for demonstrating the `timed` decorator.

    Args:
        n (int, optional): The number of times to loop. Defaults to 10^6.

    Returns:
        None. The function executes without returning a value.
    """
    for i in range(n):
        pass  # Perform the loop
