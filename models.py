# table definition

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    phone = Column(String)
    goal = Column(String)
    training_history = Column(String)
    skill_level = Column(String)
    preferences = Column(String)
    injuries = Column(String)
    special_needs = Column(String)

    def __str__(self):
        return f"Client {self.first_name} {self.last_name}, goal: {self.goal}"
