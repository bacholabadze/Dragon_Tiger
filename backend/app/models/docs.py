from typing import List
from beanie import Document


class User(Document):
    email: str
    password: str
    balance: str


class Game(Document):
    table_name: str
    min_bet: float
    max_bet: float


class Round(Document):
    game_id: str
    start_time: int
    end_time: str
    dragon_card: str
    tiger_card: str
    winner: str
    card_count: int
    finished: bool


class Player(Document):
    game_id: str                        #Sad tamashobs
    round_id: str                       #Romel raundshi tamashoba
    total_bet: float                    #Sul ramdeni aqvs dadebuli
    dragon_bet: List[int]               #Pirvel Kartze Dadebuli Betebi
    tiger_bet: List[int]                #Meore Kartze Dadebuli Betebi
    tie_bet: List[int]                  #Freze Dadebuli Betebi
    total_win: float                    #Sul Mogebuli Tanxa