"""
Client Manager

Handles creation, retrieval, and deletion of client profiles.
Uses SQLAlchemy to interact with the database.
Includes validation for personal info and integrates closed-ended questions from UI.
"""

from sqlalchemy.orm import Session
from database import SessionLocal
from models import Client
from app.ui import (
    select_goal,
    select_skill_level,
    select_preferences,
    select_training_history,
    select_injuries,
    select_special_needs,
)
import re


def get_name(prompt):
    """Prompt user for a name (first or last). Only letters allowed."""
    while True:
        name = input(prompt).strip()
        if name.isalpha():
            return name
        print("Invalid input. Please enter letters only.")


def get_phone_number():
    """
    Prompt user for phone number.
    Accepts only digits, optionally starting with '+'.
    Must be between 7 and 15 digits (excluding '+').
    """

    while True:
        phone = input("Enter phone number: ").strip()
        digits_only = phone[1:] if phone.startswith("+") else phone

        if digits_only.isdigit() and 7 <= len(digits_only) <= 15:
            return phone
        print(
            "Invalid phone number. Must be 7–15 digits, optionally starting with '+'."
        )


def get_email(session: Session):
    """Prompt user for email and check uniqueness in the database."""
    email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    while True:
        email = input("Enter email: ").strip()
        if not re.match(email_pattern, email):
            print("Invalid email format. Please enter a valid email.")
            continue
        existing = session.query(Client).filter_by(email=email).first()
        if existing:
            print("Email already exists. Please enter a different email.")
            continue
        return email


def get_personal_info(session: Session):
    """Prompt user for first name, last name, email, and phone number with validation."""
    first_name = get_name("Enter first name: ")
    last_name = get_name("Enter last name: ")
    email = get_email(session)
    phone = get_phone_number()
    return first_name, last_name, email, phone


def print_client_summary(client: Client):
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
    print_client_summary(new_client)
    print()
    session.close()
    return new_client


def list_all_profiles():
    """List all client profiles with basic info: name, email, phone."""
    session = SessionLocal()
    clients = session.query(Client).all()
    if not clients:
        print("\nNo profiles found.")
    else:
        print("\n-- Existing Client Profiles --")
        for client in clients:
            print(
                f"{client.first_name} {client.last_name} | Email: {client.email} | Phone: {client.phone}"
            )
        print("-------------------------------")
        print()
    session.close()


def open_existing_profile():
    """Open an existing client profile by email and display it."""
    session = SessionLocal()
    print()
    email = input("Enter email of the profile to open: ").strip()
    client = session.query(Client).filter_by(email=email).first()
    if client:
        print("\n-- Client profile --")
        print_client_summary(client)
        print()
    else:
        print("Profile not found.")
    session.close()


def edit_existing_profile():
    """Edit an existing client profile by updating selected fields using yes/no prompts."""
    session = SessionLocal()
    email = input("\nEnter email of the profile to edit: ").strip()
    client = session.query(Client).filter_by(email=email).first()

    if not client:
        print("Profile not found.\n")
        session.close()
        return

    print("\n-- Current Profile Data --")
    print_client_summary(client)
    print("--------------------------\n")

    def ask_yes_no(question: str) -> bool:
        while True:
            print()
            choice = input(f"{question} (yes/no): ").strip().lower()
            if choice == "yes":
                return True
            elif choice == "no":
                return False
            else:
                print("Please answer 'yes' or 'no'.")

    if ask_yes_no("Do you want to update first name?"):
        client.first_name = get_name("Enter new first name: ")

    if ask_yes_no("Do you want to update last name?"):
        client.last_name = get_name("Enter new last name: ")

    if ask_yes_no("Do you want to update phone number?"):
        client.phone = get_phone_number()

    if ask_yes_no("Do you want to update email?"):
        client.email = get_email(session)

    if ask_yes_no("Do you want to update goal?"):
        client.goal = select_goal()

    if ask_yes_no("Do you want to update skill level?"):
        client.skill_level = select_skill_level()

    if ask_yes_no("Do you want to update preferences?"):
        client.preferences = select_preferences()

    if ask_yes_no("Do you want to update training history?"):
        client.training_history = select_training_history()

    if ask_yes_no("Do you want to update injuries?"):
        client.injuries = select_injuries()

    if ask_yes_no("Do you want to update special needs?"):
        client.special_needs = select_special_needs()

    session.commit()
    print("\nProfile updated successfully!\n")
    session.close()


def delete_existing_profile():
    """Delete a profile from the database by email."""
    session = SessionLocal()
    email = input("Enter email of the profile to delete: ").strip()
    client = session.query(Client).filter_by(email=email).first()

    if client:
        while True:
            confirm = (
                input(
                    f"Are you sure you want to delete {client.first_name} {client.last_name}? (yes/no): "
                )
                .strip()
                .lower()
            )
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
