from fastapi import FastAPI

from app.db.init_db import create_all, delete_all


delete_all()
create_all()

app = FastAPI(title="Ecommerce")
