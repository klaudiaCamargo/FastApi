from fastapi import FastAPI
from app.models import models
from app.database.database import engine
from app.routers.routers import router


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router, prefix="/users", tags=["Separando Rotas Users"]) # exemplo de criacao de tag para melhor organizacao no sweguer


