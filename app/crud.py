from sqlalchemy.orm import Session
from app import models, schemas

def criar_paciente(db: Session, paciente: schemas.PacienteCreate):
    db_paciente = models.Paciente(**paciente.dict())
    db.add(db_paciente)
    db.commit()
    db.refresh(db_paciente)
    return db_paciente

def criar_profissional(db: Session, profissional: schemas.ProfissionalCreate):
    db_prof = models.Profissional(**profissional.dict())
    db.add(db_prof)
    db.commit()
    db.refresh(db_prof)
    return db_prof

def criar_consulta(db: Session, consulta: schemas.ConsultaCreate):
    db_consulta = models.Consulta(**consulta.dict())
    db.add(db_consulta)
    db.commit()
    db.refresh(db_consulta)
    return db_consulta
