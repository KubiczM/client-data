"""
Main entry point for ClientDATA.

Displays the welcome menu and routes user actions to the client manager:
- Create a new profile
- Open an existing profile
- Delete a profile
"""


from app.ui import welcome_menu
from app.client_manager import create_client_profile, open_existing_profile, delete_existing_profile

def main():
    while True:
        choice = welcome_menu()

        if choice == "1":
            create_client_profile()
        elif choice == "2":
            open_existing_profile()
        elif choice == "3":
            delete_existing_profile()
        elif choice == "0":
            print("Exiting ClientDATA. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 0, 1, 2 or 3.")

if __name__ == "__main__":
    main()
