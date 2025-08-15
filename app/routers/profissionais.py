from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import SessionLocal
router = APIRouter()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@router.post('/profissionais', tags=['Profissionais'])
def criar_profissional(profissional: schemas.ProfissionalCreate, db: Session = Depends(get_db)):
    try:
        return crud.criar_profissional(db, profissional)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
@router.get('/profissionais', tags=['Profissionais'])
def listar_profissionais(db: Session = Depends(get_db)):
    return crud.listar_profissionais(db)
@router.delete('/profissionais/{profissional_id}', tags=['Profissionais'])
def deletar_profissional(profissional_id: int, db: Session = Depends(get_db)):
    deleted = crud.deletar_profissional(db, profissional_id)
    if deleted:
        return {'deleted': profissional_id}
    raise HTTPException(status_code=404, detail='Profissional not found')
