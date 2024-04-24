import time
from uuid import uuid4

user_delay = {}

def delay_decorator(func):
    """
    A decorator to implement a delay mechanism based on a unique user identifier.

    This decorator increases the delay time for a specific user each time the function is called. 
    The delay is based on the user ID provided in the keyword arguments. It doubles the delay on each subsequent call for the same user, with a minimum delay of 1 second.

    Args:
        func (callable): The function to wrap with the delay mechanism.

    Returns:
        callable: A wrapped function that introduces a delay before executing the original function.
    """
    def wrapper(*args, **kwargs):
        # Retrieve the current delay for the user from the dictionary, defaulting to 0 if not found
        delay = user_delay.get(kwargs.get("user_id"), 0)
        
        # Double the delay for the next call, with a minimum of 1 second
        user_delay[kwargs.get("user_id")] = max(1, delay * 2)
        
        if delay > 0:
            # Notify the user about the delay before download
            print(f"Your download will start in {delay} seconds")
        
        # Introduce the delay before executing the function
        time.sleep(delay)
        
        return func(*args, **kwargs)
    
    return wrapper


@delay_decorator
def download(user_id, resource):
    """
    Simulates downloading a resource with a unique user-based delay.

    This function generates a unique download link and introduces a delay for the specified user based on their previous download attempts. 
    The delay is managed by the `delay_decorator`, which doubles the delay on each subsequent call for the same user.

    Args:
        user_id (str): The identifier for the user requesting the download.
        resource (str): The name of the resource to download.

    Returns:
        str: A message containing the download link.
    """
    download_uuid = uuid4()  # Generate a unique identifier for the download
    download_url = f"webdev2123.com/{download_uuid}"  # Create a download link using the UUID
    
    return f"Your resource is ready at: {download_url}"
