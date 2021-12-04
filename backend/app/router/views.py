from fastapi import APIRouter, Depends, HTTPException, status
from datetime import datetime, timedelta

from fastapi.security import OAuth2PasswordRequestForm
from ..configurations.app_config import settings

from ..models.docs import User, Game, Round, Player
from ..models.user_out import UserOut
from ..services.auth import get_password_hash
from ..services.auth import authenticate_user
from ..services.auth import create_access_token

router = APIRouter(prefix="")

time_stamp_now = datetime.timestamp(datetime.now())

'''
---------------------------User-------------------------------------------------------
'''


@router.post("/signup", status_code=201, response_model=UserOut, tags=['User'])
async def user_signup(user_data: User):
    user_data.password = get_password_hash(user_data.password)
    return await user_data.save()


@router.post("/token", tags=['User'])
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=int(settings.ACCESS_TOKEN_EXPIRE_MINUTES))
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token}


'''
---------------------------Game-------------------------------------------------------
'''


@router.post("/create/game", tags=['Game'], status_code=201, response_model=Game)
async def create_game(item: Game):
    return await item.save()


@router.get('/get/games', tags=['Game'])
async def get_games():
    return await Game.find_all().to_list()


@router.delete('/delete/games', tags=['Game'])
async def delete_games():
    return await Game.delete_all()


'''
------------------------Round----------------------------------------------------------
'''


@router.post('/round', tags=['Round'])
async def new_round(round_new: Round, game_id: str):
    round_new.game_id = 'test123'
    round_new.start_time = time_stamp_now
    round_new.end_time = round_new.start_time + 30
    round_new.dragon_card = ''  # For Testing Purposes
    round_new.tiger_card = ''  # For Testing Purposes
    round_new.winner = ''  # For Testing Purposes
    return await round_new.save()


@router.get('/get/rounds', tags=['Round'])
async def get_rounds():
    return await Round.find_all().to_list()


@router.delete('/delete/rounds', tags=['Round'])
async def delete_rounds():
    return await Round.delete_all()


'''
------------------------Player----------------------------------------------------------
'''


@router.get("/get/players", tags=['Player'])
async def get_players():
    return await Player.find_all().to_list()


@router.delete("/delete/players", tags=['Player'])
async def delete_all():
    return await Player.delete_all()
