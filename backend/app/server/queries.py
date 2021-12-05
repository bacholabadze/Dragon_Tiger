from datetime import datetime
from ..models.docs import Round, Player


async def get_or_create_game_round(game_id: str):
    # game_round = await Round.find_one(Round.round_id == game_id)
    # if game_round:
    #     return game_round

    game_round = Round(round_id=game_id, end_time=datetime.timestamp(datetime.now()) + 15)
    return await game_round.save()


async def get_or_create_player(game_round: str):
    player = await Player.find_one(Player.game_id == game_round)

    if player:
        return player

    player = Player(game_id=game_round)
    return await player.save()


async def winner_payment(game_round):
    async for player in Player.find(Player.game_id == str(game_round.id), Player.total_bet > 0):
        if game_round.winner == 'dragon' and player.dragon_bet > 0:
            player.balance += player.dragon_bet * 2
        if game_round.winner == 'tiger' and player.tiger_bet > 0:
            player.balance += player.tiger_bet * 2
        if game_round.winner == 'tie' and player.tiger_bet > 0:
            player.balance += player.tiger_bet * 11
        print(f'[!] player: {player}')
        await player.save()
