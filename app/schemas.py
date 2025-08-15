from pydantic import BaseModel
from typing import Optional
class PacienteCreate(BaseModel):
    id: Optional[int] = None
    nome: str
    cpf: str
class ProfissionalCreate(BaseModel):
    id: Optional[int] = None
    nome: str
    especialidade: str
class ConsultaCreate(BaseModel):
    id: Optional[int] = None
    paciente_id: int
    profissional_id: int
    data: str
