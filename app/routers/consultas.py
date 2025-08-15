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
@router.post('/consultas', tags=['Consultas'])
def criar_consulta(consulta: schemas.ConsultaCreate, db: Session = Depends(get_db)):
    try:
        return crud.criar_consulta(db, consulta)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
@router.get('/consultas', tags=['Consultas'])
def listar_consultas(db: Session = Depends(get_db)):
    return crud.listar_consultas(db)
@router.delete('/consultas/{consulta_id}', tags=['Consultas'])
def deletar_consulta(consulta_id: int, db: Session = Depends(get_db)):
    deleted = crud.deletar_consulta(db, consulta_id)
    if deleted:
        return {'deleted': consulta_id}
    raise HTTPException(status_code=404, detail='Consulta not found')
