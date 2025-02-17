# database connection support

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DB_USER, DB_PASSWORD, DB_NAME, DB_PORT
from ssh_tunnel import start_ssh_tunnel

# tunnel ssh
tunnel = start_ssh_tunnel()

# silnik bazy danych SQLAlchemy
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@127.0.0.1:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

# sesja
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
