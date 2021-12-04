from datetime import datetime
from ..models.docs import Round, Player


async def get_or_create_game_round(game_id: str):
    game_round = await Round.find_one(Round.game_id == game_id,
                                      Round.end_time > datetime.timestamp(datetime.now()))
    if game_round:
        return game_round

    game_round = Round(game_id=game_id, end_time=datetime.timestamp(datetime.now()) + 15)
    return await game_round.save()


async def get_or_create_player(game_round: str):
    player = await Player.find_one(Player.round_id == game_round)

    if player:
        return player

    player = Player(game_id=game_round, round_id=game_round)
    return await player.save()
