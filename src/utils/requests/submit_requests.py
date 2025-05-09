from fastapi.encoders import jsonable_encoder
from src.config.db_configuration import sessions
from src.utils.responses.responses import notFoundResponse, createSuccessResponse, updateSuccessResponse, deleteResponse


# Add Data
def AddData(model, request, model_name):
    # date = {
    #     "created_at": "dddd",
    #     "updated_at": "ddddd"
    # }
    # data = jsonable_encoder(request).update(date)
    # print("data", data)
    hero = model.model_validate(request)
    print("hero", hero)
    sessions.add(hero)
    print("hero_1", hero)
    sessions.commit()
    print("hero_2", hero)
    sessions.close()
    # return request
    return createSuccessResponse(data=request, model_name=model_name)


# Update Data
def UpdateData(model, request, id, model_name):
    with sessions as session:
        db_hero = session.get(model, id)
        if not db_hero:
            return notFoundResponse()
        hero_data = request.model_dump(exclude_unset=True)
        db_hero.sqlmodel_update(hero_data)
        session.add(db_hero)
        session.commit()
        session.refresh(db_hero)
        return updateSuccessResponse(data=hero_data, model_name=model_name)



# Delete Data
def DeleteData(model, id, model_name):
    with sessions as session:
        hero = session.get(model, id)
        if not hero:
            return notFoundResponse()
        session.delete(hero)
        session.commit()
        return deleteResponse(model_name=model_name)