from src.modules.user.model import User
from src.utils.router import router
from src.utils.requests.get_requests import GetAllData

# Define the router for user-related endpoints
user_router = router


@user_router.get("/users")
async def get_users():
    model = User
    return GetAllData(model, "User")