from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


def getResponse(data, model_name):
    item = {"message": f"{ model_name} get successfully",  "data": jsonable_encoder(data)}
    # return item
    return JSONResponse(
        status_code=404,
        content=item,
    )

def notFoundResponse():
    return JSONResponse(
        status_code=404,
        content={"message": f"Item not found"},
    )

def createSuccessResponse(data, model_name):
    item = {"message":  f"{model_name} created successfully" ,"data": jsonable_encoder(data)}
    # return item
    return JSONResponse(status_code=201, content=item)

def updateSuccessResponse(data, model_name):
    item = {"message": f"{model_name} data updated successfully" ,"data": jsonable_encoder(data)}
    # return item
    return JSONResponse(status_code=200, content=item)

def deleteResponse(model_name):
    item = {"message": f"{model_name} data deleted successfully" }
    return JSONResponse(status_code=200, content=item)