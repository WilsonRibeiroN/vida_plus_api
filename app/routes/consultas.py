from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import SessionLocal

router = APIRouter(prefix="/consultas", tags=["Consultas"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def criar_consulta(consulta: schemas.ConsultaCreate, db: Session = Depends(get_db)):
    return crud.criar_consulta(db, consulta)
