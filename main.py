from typing import Union
from fastapi import FastAPI
import os
from dotenv import load_dotenv
load_dotenv()
from fastapi.middleware.cors import CORSMiddleware

import config.Notion as Notion
from schemas.notion import certificateEntitys

app = FastAPI()

NotionKey=os.getenv('NotionKey')

# Configuración de CORS
origins = [
    "https://certificados.ceniteg.com"
    # Agrega tu URL de desarrollo local aquí
    # Puedes agregar más orígenes permitidos según tus necesidades
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hiiii": ":)"}

@app.get("/certificates")
def certificates(filter: Union[str, None] = "hash", value: Union[str, None] = ""):
    certificates = Notion.certificateQuery(filter, str(value))
    return certificates
