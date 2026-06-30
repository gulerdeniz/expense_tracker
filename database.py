from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

## Database bağlantısını yönetiyoruz.
DATABASE_URL = "sqlite:///./expenses.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False}) ##database bağlanma -> sqlite3'teki conn aynısı.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) ##sqlite3'teki conn, cursor, commit 3'lüsünün tekleşmiş hali.

Base = declarative_base() #Sözleşme hazırlanıyor. Bu class'tan türeyen her obje bu sözleşmeye dahil olacak.

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()