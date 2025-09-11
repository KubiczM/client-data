"""
Client Management System

This script allows adding and retrieving clients from a personal trainer's database.
It uses SQLAlchemy for database interactions.

Functions:
- add_client: Adds a new client if the email is unique.
- get_clients: Retrieves all clients from the database.

Usage:
Run the script and follow the prompts to add a new client.
"""

from database import SessionLocal, close_resources
from models import Client
import re
import sys

def validate_email(email):
    return "@" in email and "." in email

def validate_phone(phone):
    return phone.isdigit() and 6 <= len(phone) <= 15

def add_client(
    first_name,
    last_name,
    email,
    phone,
    goal,
    training_history,
    skill_level,
    preferences,
    injuries,
    special_needs,
):
    if not first_name or not last_name or not email or not goal:
        print("First name, last name, email, and goal are required!")
        return False

    if not validate_email(email):
        print("Invalid email format!")
        return False

    if phone and not validate_phone(phone):
        print("Invalid phone number!")
        return False

    with SessionLocal() as session:
        existing_client = session.query(Client).filter_by(email=email).first()
        if existing_client:
            print(f"Client with email {email} already exists!")
            return False

        new_client = Client(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            goal=goal,
            training_history=training_history,
            skill_level=skill_level,
            preferences=preferences,
            injuries=injuries,
            special_needs=special_needs,
        )
        session.add(new_client)
        session.commit()
        print(f"Client {first_name} {last_name} added successfully!")
        return True


def get_clients():
    with SessionLocal() as session:
        clients = session.query(Client).all()
        return clients


if __name__ == "__main__":
    try:
        while True:
            first_name = input("First name: ").strip()
            last_name = input("Last name: ").strip()
            email = input("Email: ").strip()
            phone = input("Phone number: ").strip()
            goal = input("Goal: ").strip()
            training_history = input("Training history: ").strip()
            skill_level = input("Skill level: ").strip()
            preferences = input("Preferences: ").strip()
            injuries = input("Injuries: ").strip()
            special_needs = input("Special needs: ").strip()

            if add_client(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                goal=goal,
                training_history=training_history,
                skill_level=skill_level,
                preferences=preferences,
                injuries=injuries,
                special_needs=special_needs,
            ):
                break

        print("\nAll clients in the database:")
        clients = get_clients()
        for client in clients:
            print(client)
    finally:
        close_resources()
