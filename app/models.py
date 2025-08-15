from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
class Paciente(Base):
    __tablename__ = 'pacientes'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    cpf = Column(String(20), unique=True, nullable=True)
class Profissional(Base):
    __tablename__ = 'profissionais'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    especialidade = Column(String(100), nullable=True)
class Consulta(Base):
    __tablename__ = 'consultas'
    id = Column(Integer, primary_key=True, index=True)
    paciente_id = Column(Integer, ForeignKey('pacientes.id'))
    profissional_id = Column(Integer, ForeignKey('profissionais.id'))
    data = Column(String(100))
    paciente = relationship('Paciente')
    profissional = relationship('Profissional')
