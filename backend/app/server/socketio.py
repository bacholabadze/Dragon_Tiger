import socketio
from beanie import PydanticObjectId
from urllib.parse import parse_qs
from ..models.docs import Game, Round, Player
from .queries import get_or_create_game_round
from ..game.gamelogics import find_winner

sio = socketio.AsyncServer(async_mode="asgi", cors_allowed_origins=[])
sio_app = socketio.ASGIApp(sio)


@sio.event
async def connect(sid, environ):
    game_id = parse_qs(environ['QUERY_STRING']).get("game_id")[0]
    game = await Game.get(PydanticObjectId(game_id))
    game_round = await get_or_create_game_round(game_id)
    send_data = {
        "name": game.table_name,
        "game_round_id": str(game_round.id),
        "max_bet": game.max_bet,
        "min_bet": game.min_bet,
        "start_timestamp": 15
    }
    sio.enter_room(sid, game_id)
    await sio.emit("on_connect_data", send_data, to=sid)
    print("Shemovdivar Otaxshi.")


@sio.event
async def disconnect(sid):
    print("Aba he")


@sio.event
async def scan_card(sid, data):
    print(data)
    game_round = await Round.get(PydanticObjectId(data['game_round_id']))
    card = data['card']
    if game_round.card_count % 2:
        game_round.tiger_card = card
        game_round.card_count += 1
        await game_round.save()
        await sio.emit("send_tiger_card", {"card": card}, room=game_round.game_id)
    else:
        game_round.dragon_card = card
        game_round.card_count += 1
        await game_round.save()
        await sio.emit("send_dragon_card", {"card": card}, room=game_round.game_id)

    if game_round.card_count == 2:
        dragon_card = game_round.dragon_card
        tiger_card = game_round.tiger_card
        winner = find_winner(dragon_card, tiger_card)
        game_round.winner = winner
        game_round.finished = True
        await game_round.save()


@sio.event
async def place_bet(sid, data):
    amount = int(data.get('amount'))
    card_type = data.get('type')
    game_round = await Round.get(PydanticObjectId(data.get('game_round_id')))
    player = Player(game_id=game_round.game_id)

    if card_type == "tiger":
        player.tiger_bet = amount
        await player.save()
    elif card_type == "dragon":
        player.dragon_bet = amount
        await player.save()
    else:
        player.tie_bet = amount
        await player.save()

