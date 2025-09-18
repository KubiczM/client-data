"""
Database connection setup.

Creates SQLAlchemy engine and session.
Optionally sets up SSH tunnel for remote database access.
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DB_USER, DB_PASSWORD, DB_NAME
from ssh_tunnel import start_ssh_tunnel, stop_ssh_tunnel

tunnel, LOCAL_PORT = start_ssh_tunnel()

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@127.0.0.1:{LOCAL_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def close_resources():
    stop_ssh_tunnel(tunnel)

