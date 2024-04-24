import time
from functools import wraps
from random import randint

# Dictionary for caching weather data with city as the key
cache = {}

def cache_decorator(func):
    """
    A decorator for caching the result of a function to improve performance.

    This decorator caches the result of a function call based on a key (e.g., a city name). 
    If the cached data for a given key is still valid (within a specified time limit), 
    the cached result is returned. Otherwise, the original function is called to get the new result, 
    which is then cached with a timestamp.

    Args:
        func (callable): The function to be decorated with caching.

    Returns:
        callable: A wrapped function that caches results based on a key and a time limit.
    """
    @wraps(func)
    def wrapper(city):
        # Check if the city is in the cache and if the cache is still valid (within 10 seconds)
        if city in cache and time.time() - cache[city]['time'] < 10:
            print(f"Returning cached result for {city}...")
            return cache[city]['data']

        # If not, call the original function and update the cache
        result = func(city)
        cache[city] = {
            "data": result,
            "time": time.time()  # Store the current time with the cached data
        }

        return result
    
    return wrapper


@cache_decorator
def get_weather(city):
    """
    Simulates fetching weather data for a given city.

    This function, decorated with a caching mechanism, fetches weather data for a specified city. 
    If the result is cached and still valid, it retrieves the cached data; otherwise, it simulates fetching new weather data.

    Args:
        city (str): The name of the city for which to fetch weather data.

    Returns:
        dict: A dictionary containing weather information like temperature and humidity.
    """
    print(f"Fetching weather data for {city}...")
    
    # Simulate a delay to mimic real-world data fetching
    time.sleep(1)

    weather_data = {
        'temperature': randint(-10, 30),  # Random temperature between -10 and 30 degrees
        'humidity': randint(0, 100)  # Random humidity between 0 and 100%
    }

    return weather_data




