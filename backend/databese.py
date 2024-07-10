from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Dane do połączenia z bazą danych PostgreSQL
SQLALCHEMY_DATABASE_URL = "postgresql://currency:4Helx7lo@localhost:5432/currency"

# Utworzenie silnika bazy danych
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Utworzenie klasy bazowej do deklaratywnego tworzenia modeli
Base = declarative_base()

# Utworzenie klasy sesji do zarządzania sesjami
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
