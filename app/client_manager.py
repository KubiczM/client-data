"""
Client Manager

Handles creation, retrieval, and deletion of client profiles.
Uses SQLAlchemy to interact with the database.
Includes validation for personal info and integrates closed-ended questions from UI.
"""


from app.ui import (
    select_goal,
    select_skill_level,
    select_preferences,
    select_training_history,
    select_injuries,
    select_special_needs
)

from database import SessionLocal
from models import Client


def is_email_unique(session, email):
    """Check if email already exists in the database."""
    existing = session.query(Client).filter_by(email=email).first()
    return existing is None

def get_personal_info(session):
    """Prompt user for personal info with basic validation."""
    while True:
        first_name = input("Enter first name: ").strip()
        last_name = input("Enter last name: ").strip()
        email = input("Enter email: ").strip()
        phone = input("Enter phone number: ").strip()

        if not first_name or not last_name or not email:
            print("First name, last name, and email are required. Try again.")
            continue

        if not is_email_unique(session, email):
            print("Email already exists. Try a different one.")
            continue

        return first_name, last_name, email, phone

def create_client_profile():
    """Create a new client profile and save it to the database."""
    session = SessionLocal()
    print("\n-- Creating a new profile --")
    first_name, last_name, email, phone = get_personal_info(session)

    goal = select_goal()
    skill_level = select_skill_level()
    preferences = select_preferences()
    training_history = select_training_history()
    injuries = select_injuries()
    special_needs = select_special_needs()

    new_client = Client(
        first_name=first_name,
        last_name=last_name,
        email=email,
        phone=phone,
        goal=goal,
        skill_level=skill_level,
        preferences=preferences,
        training_history=training_history,
        injuries=injuries,
        special_needs=special_needs,
    )

    session.add(new_client)
    session.commit()
    print("\nProfile created successfully!")
    print_client_summary(Client)
    session.close()
    return new_client


def open_existing_profile():
    """Open an existing profile from the database."""
    session = SessionLocal()
    email = input("Enter email of the profile to open: ").strip()
    client = session.query(Client).filter_by(email=email).first()


    if client:
        print("\nProfile found:")
        print_client_summary(client)
        session.close()
        return client

    print("Profile not found.")
    session.close()
    return None

def delete_existing_profile():
    """Delete a profile from the database by email."""
    session = SessionLocal()
    email = input("Enter email of the profile to delete: ").strip()
    client = session.query(Client).filter_by(email=email).first()

    if client:
        while True:
            confirm = input(f"Are you sure you want to delete {client.first_name} {client.last_name}? (yes/no): ").strip().lower()
            if confirm == "yes":
                session.delete(client)
                session.commit()
                print("Profile deleted successfully.")
                break
            elif confirm == "no":
                print("Deletion cancelled.")
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
    else:
        print("Profile not found.")
    session.close()




def print_client_summary(client):
    """Print client info."""
    print("-----------------------------")
    print(f"Name: {client.first_name} {client.last_name}")
    print(f"Email: {client.email}")
    print(f"Phone: {client.phone}")
    print(f"Goal: {client.goal}")
    print(f"Skill Level: {client.skill_level}")
    print(f"Preferences: {client.preferences}")
    print(f"Training History: {client.training_history}")
    print(f"Injuries: {client.injuries}")
    print(f"Special Needs: {client.special_needs}")
    print("-----------------------------")