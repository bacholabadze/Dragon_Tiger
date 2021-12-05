import socketio
from beanie import PydanticObjectId
from urllib.parse import parse_qs
from ..models.docs import Game, Round, Player
from .queries import get_or_create_game_round, get_or_create_player, winner_payment
from ..game.gamelogics import find_winner, place_bets

sio = socketio.AsyncServer(async_mode="asgi", cors_allowed_origins=[])
sio_app = socketio.ASGIApp(sio)


@sio.event
async def connect(sid, environ):
    print("\n\n\nShemovdivar Otaxshi.")
    game_id = parse_qs(environ['QUERY_STRING']).get("game_id")[0]
    print({"[!] game_id ": game_id})
    game = await Game.get(PydanticObjectId(game_id))
    print(f'[!] game : {game}')
    game_round = await get_or_create_game_round(game_id)
    print(f'[!] game_round: {game_round}')
    send_data = {
        "name": game.name,
        "game_round_id": str(game_round.id),
        "max_bet": game.max_bet,
        "min_bet": game.min_bet,
        "start_timestamp": 15
    }
    print(f'[!] data sent: {send_data}')
    sio.enter_room(sid, game_id)
    await sio.emit("on_connect_data", send_data, to=sid)
    print("[V] Shemovedi uprobl.\n\n")


@sio.event
async def scan_card(sid, data):
    print('[!] Scan_Card.')
    print(f'[!] Data received: {data}')
    game_round_id = data.get('game_round_id')
    print(f'[!] game_round_id :{game_round_id}')
    game_round = await Round.get(PydanticObjectId(game_round_id))
    print(f'[!] game_round: {game_round}')
    player = await get_or_create_player(game_round_id)
    print(f'[!] player: {player}')

    card = data['card']
    print(f'[!] card received : {card}')

    if game_round.card_count == 0:
        game_round.dragon_card = card
        game_round.card_count += 1
        await game_round.save()
        await sio.emit("send_dragon_card", {"card": card}, room=game_round.round_id)
        print(f'[!] Dragon Card: {game_round.dragon_card}')
        print(f'[!] card_count: {game_round.card_count}')
    else:
        game_round.tiger_card = card
        game_round.card_count += 1
        await game_round.save()
        await sio.emit("send_tiger_card", {"card": card}, room=game_round.round_id)
        print(f'[!] Tiger Card: {game_round.tiger_card}')

    if game_round.tiger_card is not None:
        dragon_card = game_round.dragon_card
        tiger_card = game_round.tiger_card
        winner = find_winner(dragon_card, tiger_card)
        print(f'[!] Winner : {winner}')
        game_round.winner = winner
        game_round.finished = True
        game_round.card_count = 0
        await game_round.save()

    await winner_payment(game_round)
    print('\t[!] Scanned Successfully')


@sio.event
async def place_bet(sid, data):
    print(f'[!] [data] = {data}')
    amount = int(data.get('amount'))
    print(f'[!] amount = {amount}')
    card_type = data.get('type')
    print(f'[!] card_type = {card_type}')
    round_id = data.get('game_round_id')

    player = await get_or_create_player(round_id)
    print(f'[!] player = {player}')
    await place_bets(player, card_type, amount)


@sio.event
async def disconnect(sid):
    print("Aba he")
