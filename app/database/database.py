from sqlalchemy import  create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import  sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}   # <<------ só para SQLite
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)  # <<------ criando a sessao local

Base = declarative_base() # <<------ instanciando base para criar classes