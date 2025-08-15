# 🏥 SGHSS - VidaPlus API

Sistema de Gestão Hospitalar e de Serviços de Saúde (SGHSS), desenvolvido como parte do Projeto Multidisciplinar - 2025A1 da UNINTER.

---

## 🚀 Tecnologias Utilizadas

- 🐍 Python 3.11+
- ⚡ [FastAPI](https://fastapi.tiangolo.com/)
- 🐘 MySQL 9
- 🛠️ SQLAlchemy
- 🔐 Pydantic
- 🔄 Uvicorn
- ⚙️ jinja2

---

## 📦 Instalação

### ✅ Pré-requisitos

- Python 3 instalado
- MySQL instalado
- Git instalado

### 📥 Clone o repositório

```bash
git clone https://github.com/WilsonRibeiroN/vida_plus_api.git
cd vida_plus_api
```

### 🐍 Crie e ative o ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 📦 Instale as dependências

```bash
pip install -r requirements.txt
```

### ⚙️ Configure o banco de dados

1. Crie o banco no MySQL:

```sql
CREATE DATABASE vida_plus;
use vida_plus;
```

2. Configure o arquivo `.env`:

```
MYSQL_USER=sghss
MYSQL_PASSWORD=123456
MYSQL_DB=vida_plus
MYSQL_HOST=localhost
```

### ▶️ Rode a aplicação

```bash
uvicorn app.main:app --reload
```

---

## 🔌 Endpoints disponíveis

- `POST /pacientes/` - Criar paciente
- `POST /profissionais/` - Criar profissional
- `POST /consultas/` - Agendar consulta
- `GET /pacientes/` - Listar pacientes
- `GET /profissionais/` - Listar profissionais
- `GET /consultas/` - Listar consultas
- `DELETE /pacientes/` - Deletar paciente
- `DELETE  /profissionais/` - Deletar profissional
- `DELETE  /consultas/` - Deletar consulta

---

## 🧪 Testes

Acesse a documentação interativa:

- Principal: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- Swagger: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📄 Licença

Este projeto foi desenvolvido para fins acadêmicos no curso de Análise e Desenvolvimento de Sistemas da UNINTER.

---

## 👤 Autor

- **Wilson Ribeiro Nazario**
- RU: 4477518
- GitHub: [@WilsonRibeiroN](https://github.com/WilsonRibeiroN)
