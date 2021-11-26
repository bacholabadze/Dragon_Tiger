from typing import List, Optional

class Game:
    game_id: str
    table_name: str
    min_bet: int
    max_bet: str


class Round:
    game_id: str
    round_time: Optional[str]  
    dragon_card: str
    tiger_card: str
    winner: str
    card_count: int
    finished: bool


class Player:
    game_id: str                        #Sad tamashobs
    game_round: List[int]               #Romel raundshi tamashoba
    total_bet: int                      #Sul ramdeni aqvs dadebuli
    dragon_bet: List[int]               #Pirvel Kartze Dadebuli Betebi
    tiget_bet: List[int]                #Meore Kartze Dadebuli Betebi
    tie_bet: List[int]                  #Freze Dadebuli Betebi