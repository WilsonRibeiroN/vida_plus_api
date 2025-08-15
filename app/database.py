from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
load_dotenv()
DB_USER = os.getenv('MYSQL_USER','root')
DB_PASS = os.getenv('MYSQL_PASSWORD','')
DB_NAME = os.getenv('MYSQL_DB','vida_plus')
DB_HOST = os.getenv('MYSQL_HOST','localhost')
DATABASE_URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
engine = create_engine(DATABASE_URL, echo=False, pool_recycle=3600)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
