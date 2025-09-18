"""
User Interface module for ClientDATA.

Provides:
- Welcome menu
- Closed-ended questions (goal, skill level, preferences, etc.)
All questions enforce input validation and present options in a simple numeric format.
"""


def welcome_menu():
    print("===================================")
    print("  Welcome to ClientDATA! ")
    print("===================================")
    print("1. Create a new profile")
    print("2. Open an existing profile")
    print("3. Delete existing profile")
    print("0. Exit")

    choice = input("Select an option: ").strip()
    return choice


def select_skill_level():
    options = {
        "1": "Beginner",
        "2": "Intermediate",
        "3": "Advanced"
    }

    while True:
        choice = input("Select skill level (enter 1, 2, or 3): ").strip()
        if choice in options:
            print(f"Selected: {options[choice]}")
            return options[choice]
        print("Invalid choice, try again.")


def select_goal():
    options = {
        "1": "Build Muscle",
        "2": "Lose Fat",
        "3": "Increase Strength",
        "4": "Improve Endurance",
    }

    while True:
        choice = input("Select skill level (enter 1, 2, 3, or 4): ").strip()
        if choice in options:
            print(f"Selected: {options[choice]}")
            return options[choice]
        print("Invalid choice, try again.")


def select_preferences():
    options = {
        "1": "Home Workouts",
        "2": "Gym Workouts",
        "3": "Outdoor Activities",
        "4": "Group Classes",
    }

    while True:
        choice = input("Select preferences (enter 1, 2, 3, or 4): ").strip()
        if choice in options:
            print(f"Selected: {options[choice]}")
            return options[choice]
        print("Invalid choice, try again.")


def select_training_history():
    options = {
        "1": "No previous training",
        "2": "Occasional training",
        "3": "Regular training",
        "4": "Professional/Competitive",
    }

    while True:
        choice = input("Select training history (enter 1, 2, 3, or 4): ").strip()
        if choice in options:
            print(f"Selected: {options[choice]}")
            return options[choice]
        print("Invalid choice, try again.")


def select_injuries():
    options = {
        "1": "No injuries",
        "2": "Minor injuries",
        "3": "Chronic issues",
        "4": "Major injuries",
    }

    while True:
        choice = input("Select injuries (enter 1, 2, 3, or 4): ").strip()
        if choice in options:
            print(f"Selected: {options[choice]}")
            return options[choice]
        print("Invalid choice, try again.")


def select_special_needs():
    options = {
        "1": "None",
        "2": "Dietary restrictions",
        "3": "Mobility limitations",
        "4": "Other special needs",
    }

    while True:
        choice = input("Select special needs (enter 1, 2, 3, or 4): ").strip()
        if choice in options:
            print(f"Selected: {options[choice]}")
            return options[choice]
        print("Invalid choice, try again.")