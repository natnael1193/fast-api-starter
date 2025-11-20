from fastapi import APIRouter, UploadFile

def router(tag = "Default"):
    routers = APIRouter(tags=[tag])
    return routers