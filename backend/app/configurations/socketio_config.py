import socketio

sio = socketio.AsyncServer(async_mode="asgi", cors_allowed_origins=[])
sio_app = socketio.ASGIApp(sio)


@sio.event
async def connect(sid, environ):
    print("Shemovdivar Otaxshi")


@sio.event
async def disconnect(sid):
    print("Aba he")