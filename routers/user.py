from fastapi import APIRouter
from fastapi import status
from fastapi.responses import JSONResponse
from utils.jwt_manager import create_token
from schemas.user import User

user_router = APIRouter()

@user_router.post('/login',tags=['auth'],status_code=status.HTTP_200_OK)
def login(user:User):
    if (user.email == 'admin@gmail.com' and user.password == 'admin'):
        token:str = create_token(user.dict())
        return JSONResponse(status_code=status.HTTP_200_OK, content=token)
    else:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content='Credenciales inválidas')