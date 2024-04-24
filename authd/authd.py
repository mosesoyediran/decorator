from functools import wraps

# Application State
ROSTER = [
    {"name": "Alice", "votes": 12},
    {"name": "Tyler", "votes": 9},
    {"name": "Andrew", "votes": 10}
]

USERNAME = "admin"
PASSWORD = "pw"

# Set to keep track of authenticated users
AUTHD_USER = set()

def authd(func):
    """
    A decorator to enforce authentication for a function.

    If the user is not authenticated (i.e., not in the `AUTHD_USER` set), they are prompted to enter a username and password.
    If the entered credentials match the predefined `USERNAME` and `PASSWORD`, they are added to the authenticated set.
    Otherwise, an authentication failure message is displayed and the function does not execute.

    Args:
        func (callable): The function to be protected with authentication.

    Returns:
        callable: A wrapped function that enforces authentication.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        if USERNAME not in AUTHD_USER:
            entered_username = input("Enter username: ")
            entered_password = input("Enter password: ")

            if entered_password != PASSWORD or entered_username != USERNAME:
                print("Authentication failed!")
                return

            AUTHD_USER.add(entered_username)

        return func(*args, **kwargs)

    return wrapper

def menu():
    """
    Displays a menu with options to view the roster, upvote a person, add a new person to the roster, or quit.

    Based on user input, calls the appropriate function to perform the desired action.
    """
    while True:
        print("""
        a. View Roster
        b. Upvote
        c. Add to Roster
        d. Quit
        """)

        option = input("Enter option: ").lower()

        if option == "a":
            view_roster()
        elif option == "b":
            upvote()
        elif option == "c":
            add_to_roster()
        else:
            break

def view_roster():
    """
    Displays the current roster, sorted by the number of votes in descending order.

    Each person in the roster is displayed along with their name and number of votes.
    """
    sorted_roster = sorted(ROSTER, key=lambda p: p["votes"], reverse=True)

    for p in sorted_roster:
        print(f"{p['name']}: {p['votes']}")

@authd
def upvote():
    """
    Allows the user to upvote a person in the roster, after authentication.

    Prompts the user to enter a name. If the name exists in the roster, it increments their vote count by one.
    If the name is not found, it displays a message indicating the name was not found.
    """
    name = input("Enter the name of the person to upvote: ").lower()

    for p in ROSTER:
        if p["name"].lower() == name:
            p["votes"] += 1
            print(f"Upvoted {p['name']}!")
            return

    print("Name was not found!")

@authd
def add_to_roster():
    """
    Allows the user to add a new person to the roster, after authentication.

    Prompts the user to enter a name, and then adds this name to the roster with an initial vote count of zero.
    """
    name = input("Enter the name of the person to add: ")
    ROSTER.append({"name": name, "votes": 0})
    print(f"Added {name} to the roster!")
