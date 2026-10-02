from app.db.database import Base, engine
from app.db import models

def init_database() -> None:
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_database()
    print("CloudSentinel database initialized successfully.")