from typing import List
from beanie import Document
from datetime import datetime


class User(Document):
    email: str
    password: str
    balance: str


class Game(Document):
    table_name: str = 'test'
    min_bet: float = '5'
    max_bet: float = '200'


class Round(Document):
    game_id: str
    end_time: float = datetime.timestamp(datetime.now()) + 15
    dragon_card: str = None
    tiger_card: str = None
    winner: str = None
    card_count: int = 0
    finished: bool = False


class Player(Document):
    game_id: str                        #Sad tamashobs
    round_id: str                       #Romel raundshi tamashoba
    total_bet: float = 0                #Sul ramdeni aqvs dadebuli
    dragon_bet: List[int] = 0           #Pirvel Kartze Dadebuli Betebi
    tiger_bet: List[int] = 0            #Meore Kartze Dadebuli Betebi
    tie_bet: List[int] = 0              #Freze Dadebuli Betebi
    total_win: float = 0                #Sul Mogebuli Tanxa
    balance: int = 100                  #Tanxis Raodenoba Balansze
