"""
Database Models.

Defines the Client table using SQLAlchemy ORM.
Includes fields for personal info, goals, skill level, preferences, injuries, and special needs.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    phone = Column(String(20))
    goal = Column(String(100), nullable=False)
    training_history = Column(String(255))
    skill_level = Column(String(50))
    preferences = Column(String(255))
    injuries = Column(String(255))
    special_needs = Column(String(255))

    def __str__(self):
        return f"Client {self.first_name} {self.last_name}, goal: {self.goal}"
