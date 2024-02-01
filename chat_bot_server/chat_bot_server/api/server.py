from chat_bot_server.containers import Container
from chat_bot_server.api.routers import chat_bot_router

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

def create_container() -> Container:
    container = Container()
    container.init_resources()
    container.wire(modules=[chat_bot_router])
    return container


def create_app() -> FastAPI:
    container = create_container()
    _app = FastAPI()
    _app.extra = {"container": container}
    _app.include_router(chat_bot_router.router)
    return _app

app = create_app()

app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=False,
        allow_methods=["*"],
        allow_headers=["*"],
    )

@app.get("/")
def index():
    return {"message": "hi im the chat bot server"}