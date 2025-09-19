"""
User Interface module for ClientDATA.

Provides:
- Welcome menu
- Closed-ended questions (goal, skill level, preferences, etc.)
All questions enforce input validation and present options clearly.
"""


def welcome_menu():
    print("===================================")
    print("  Welcome to ClientDATA! ")
    print("===================================")
    print("1. Create a new profile")
    print("2. List all profiles")
    print("3. Open an existing profile")
    print("4. Edit existing profile")
    print("5. Delete existing profile")
    print("0. Exit\n")

    return input("Select an option (type number and press Enter): ").strip()


def select_goal():
    options = {
        "1": "Build Muscle",
        "2": "Lose Fat",
        "3": "Increase Strength",
        "4": "Improve Endurance",
    }
    while True:
        print("\nSelect your goal:")
        for key, value in options.items():
            print(f"{key}. {value}")
        choice = input("Enter number: ").strip()
        if choice in options:
            return options[choice]
        print("Invalid choice, try again.")


def select_skill_level():
    options = {"1": "Beginner", "2": "Intermediate", "3": "Advanced"}
    while True:
        print("\nSelect your skill level:")
        for key, value in options.items():
            print(f"{key}. {value}")
        choice = input("Enter number: ").strip()
        if choice in options:
            return options[choice]
        print("Invalid choice, try again.")


def select_preferences():
    options = {
        "1": "Home Workouts",
        "2": "Gym Workouts",
        "3": "Outdoor Activities",
        "4": "Other",
    }
    while True:
        print("\nSelect your preferences:")
        for key, value in options.items():
            print(f"{key}. {value}")
        choice = input("Enter number: ").strip()
        if choice in options:
            return options[choice]
        print("Invalid choice, try again.")


def select_training_history():
    options = {
        "1": "No previous training",
        "2": "Some experience",
        "3": "Regular training",
        "4": "Professional/Competitive",
    }
    while True:
        print("\nSelect your training history:")
        for key, value in options.items():
            print(f"{key}. {value}")
        choice = input("Enter number: ").strip()
        if choice in options:
            return options[choice]
        print("Invalid choice, try again.")


def select_injuries():
    options = {
        "1": "No injuries",
        "2": "Minor injuries",
        "3": "Moderate injuries",
        "4": "Major injuries",
    }
    while True:
        print("\nSelect your injuries:")
        for key, value in options.items():
            print(f"{key}. {value}")
        choice = input("Enter number: ").strip()
        if choice in options:
            return options[choice]
        print("Invalid choice, try again.")


def select_special_needs():
    options = {
        "1": "None",
        "2": "Dietary restrictions",
        "3": "Medical conditions",
        "4": "Other special needs",
    }
    while True:
        print("\nSelect your special needs:")
        for key, value in options.items():
            print(f"{key}. {value}")
        choice = input("Enter number: ").strip()
        if choice in options:
            return options[choice]
        print("Invalid choice, try again.")
