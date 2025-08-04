from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import SessionLocal

router = APIRouter(prefix="/profissionais", tags=["Profissionais"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def criar_profissional(profissional: schemas.ProfissionalCreate, db: Session = Depends(get_db)):
    return crud.criar_profissional(db, profissional)
