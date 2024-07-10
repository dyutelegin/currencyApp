from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.currency import Base
from databese import SessionLocal, engine
from sqlalchemy import text


Base.metadata.create_all(bind=engine)

router = APIRouter()

# Zależność do sesji bazy danych
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint testowy
@router.get("/test-db")
def test_db_connection(db: Session = Depends(get_db)):
    try:
        # Proste zapytanie testowe
        result = db.execute(text("SELECT 1"))
        return {"status": "success", "result": result.scalar()}
    except Exception as e:
        return {"status": "error", "detail": str(e)}
