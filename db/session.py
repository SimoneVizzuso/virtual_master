import os
from sqlmodel import SQLModel, Session, create_engine
from .models import Zone, ZoneConnection

DB_FILE = os.path.join(os.path.dirname(__file__), "database.db")
engine = create_engine(f"sqlite:///{DB_FILE}", echo=True)

def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    return Session(engine)