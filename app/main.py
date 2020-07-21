from __future__ import annotations

import os
import shutil

from fastapi import FastAPI, UploadFile, File
from starlette.staticfiles import StaticFiles

from app.routers import auth, user, product, order

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.post('/upload_image/')
async def upload_avatar(file: UploadFile = File(...)):
    file_object = file.file
    # create empty file to copy the file_object to
    current_dir: str = os.getcwd()
    upload_folder = open(os.path.join(current_dir, './app/static/images', file.filename), 'wb+')
    shutil.copyfileobj(file_object, upload_folder)
    upload_folder.close()
    return {"file_url": '/app/static/images/' + file.filename}


app.include_router(auth.router)
app.include_router(user.router)
app.include_router(product.router)
app.include_router(order.router)
