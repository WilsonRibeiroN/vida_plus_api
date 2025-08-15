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
@router.post('/pacientes', tags=['Pacientes'])
def criar_paciente(paciente: schemas.PacienteCreate, db: Session = Depends(get_db)):
    try:
        return crud.criar_paciente(db, paciente)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
@router.get('/pacientes', tags=['Pacientes'])
def listar_pacientes(db: Session = Depends(get_db)):
    return crud.listar_pacientes(db)
@router.delete('/pacientes/{paciente_id}', tags=['Pacientes'])
def deletar_paciente(paciente_id: int, db: Session = Depends(get_db)):
    deleted = crud.deletar_paciente(db, paciente_id)
    if deleted:
        return {'deleted': paciente_id}
    raise HTTPException(status_code=404, detail='Paciente not found')
