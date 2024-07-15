from typing import Union
from fastapi import FastAPI
import os
from dotenv import load_dotenv
load_dotenv()

import config.Notion as Notion
from schemas.notion import certificateEntitys

app = FastAPI()

NotionKey=os.getenv('NotionKey')

@app.get("/")
def read_root():
    return {"Hiiii": ":)"}

@app.get("/certificates")
def certificates(filter: Union[str, None] = "hash", value: Union[str, None] = ""):
    certificates = Notion.certificateQuery(filter, str(value))
    return certificates
