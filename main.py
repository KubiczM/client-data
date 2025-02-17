# main application logic

from database import SessionLocal
from models import Client


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
    session = SessionLocal()

    existing_client = session.query(Client).filter_by(email=email).first()
    if existing_client:
        print(
            f"Client with email {email} already exists. Please provide different details."
        )
        session.close()
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
    session.close()
    print(f"Client {first_name} {last_name} added successfully!")
    return True


def get_clients():
    session = SessionLocal()
    clients = session.query(Client).all()
    session.close()
    return clients


if __name__ == "__main__":
    while True:
        first_name = input("First name: ")
        last_name = input("Last name: ")
        email = input("Email: ")
        phone = input("Phone number: ")
        goal = input("Goal: ")
        training_history = input("Training history: ")
        skill_level = input("Skill level: ")
        preferences = input("Preferences: ")
        injuries = input("Injuries: ")
        special_needs = input("Special needs: ")

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

    clients = get_clients()
    for client in clients:
        print(client)
