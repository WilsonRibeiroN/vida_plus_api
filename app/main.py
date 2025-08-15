# app/main.py
from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.database import engine    # certificado de que app.database está correto
from app.models import Base        # Base do SQLAlchemy
from app.routers import pacientes, profissionais, consultas  # suas routers

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(title="Vida Plus - SGHSS", version="0.1.0")

# cria tabelas se necessário
Base.metadata.create_all(bind=engine)

# arquivos estáticos e templates
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

# rota raiz
@app.get("/")
def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# incluir routers das APIs
app.include_router(pacientes.router, prefix="/api")
app.include_router(profissionais.router, prefix="/api")
app.include_router(consultas.router, prefix="/api")
