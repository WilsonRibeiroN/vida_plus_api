from fastapi import FastAPI
from app.routes import pacientes, profissionais, consultas
from app.database import Base, engine

app = FastAPI(title="Vida Plus - SGHSS")

Base.metadata.create_all(bind=engine)

app.include_router(pacientes.router)
app.include_router(profissionais.router)
app.include_router(consultas.router)
