from pydantic import BaseModel

class PacienteCreate(BaseModel):
    nome: str
    email: str
    plano_saude: str

class ProfissionalCreate(BaseModel):
    nome: str
    especialidade: str

class ConsultaCreate(BaseModel):
    paciente_id: int
    profissional_id: int
    data: str
