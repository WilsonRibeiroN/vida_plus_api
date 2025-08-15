from sqlalchemy.orm import Session
from app import models, schemas
def criar_paciente(db: Session, paciente: schemas.PacienteCreate):
    data = paciente.dict()
    if data.get('id') is not None:
        db_p = models.Paciente(id=data['id'], nome=data['nome'], cpf=data['cpf'])
    else:
        db_p = models.Paciente(nome=data['nome'], cpf=data['cpf'])
    db.add(db_p)
    db.commit()
    db.refresh(db_p)
    return db_p
def listar_pacientes(db: Session):
    return db.query(models.Paciente).all()
def deletar_paciente(db: Session, paciente_id: int):
    # apaga consultas associadas
    db.query(models.Consulta).filter(models.Consulta.paciente_id == paciente_id).delete()
    deleted = db.query(models.Paciente).filter(models.Paciente.id == paciente_id).delete()
    db.commit()
    return deleted
def criar_profissional(db: Session, profissional: schemas.ProfissionalCreate):
    data = profissional.dict()
    if data.get('id') is not None:
        db_p = models.Profissional(id=data['id'], nome=data['nome'], especialidade=data['especialidade'])
    else:
        db_p = models.Profissional(nome=data['nome'], especialidade=data['especialidade'])
    db.add(db_p)
    db.commit()
    db.refresh(db_p)
    return db_p
def listar_profissionais(db: Session):
    return db.query(models.Profissional).all()
def deletar_profissional(db: Session, profissional_id: int):
    db.query(models.Consulta).filter(models.Consulta.profissional_id == profissional_id).delete()
    deleted = db.query(models.Profissional).filter(models.Profissional.id == profissional_id).delete()
    db.commit()
    return deleted
def criar_consulta(db: Session, consulta: schemas.ConsultaCreate):
    data = consulta.dict()
    if data.get('id') is not None:
        db_c = models.Consulta(id=data['id'], paciente_id=data['paciente_id'], profissional_id=data['profissional_id'], data=data['data'])
    else:
        db_c = models.Consulta(paciente_id=data['paciente_id'], profissional_id=data['profissional_id'], data=data['data'])
    db.add(db_c)
    db.commit()
    db.refresh(db_c)
    return db_c
def listar_consultas(db: Session):
    return db.query(models.Consulta).all()
def deletar_consulta(db: Session, consulta_id: int):
    deleted = db.query(models.Consulta).filter(models.Consulta.id == consulta_id).delete()
    db.commit()
    return deleted
