"""
Main entry point for ClientDATA.

Displays the welcome menu and routes user actions to the client manager:
- Create a new profile
- Open an existing profile
- Edit or delete a profile
"""

from app.ui import welcome_menu
from app.client_manager import (
    create_client_profile,
    list_all_profiles,
    open_existing_profile,
    delete_existing_profile,
    edit_existing_profile,
)


def main():
    try:
        while True:
            choice = welcome_menu()

            if choice == "1":
                create_client_profile()
            elif choice == "2":
                list_all_profiles()
            elif choice == "3":
                open_existing_profile()
            elif choice == "4":
                edit_existing_profile()
            elif choice == "5":
                delete_existing_profile()
            elif choice == "0":
                print("Exiting ClientDATA. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 0, 1, 2, 3, 4 or 5.")
    except KeyboardInterrupt:
        print("\nExiting ClientDATA. Goodbye!")
        exit(0)


if __name__ == "__main__":
    main()
