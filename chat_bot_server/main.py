import uvicorn
from fastapi import FastAPI, UploadFile, File, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pathlib import Path
from chat_bot_server.containers import Container
from dependency_injector.wiring import Provide, inject
from chat_bot_server.services.chat_bot_service import ChatBotService
from chat_bot_server.clients.file_system_client import FileSystemClient


def create_container() -> Container:
    container = Container()
    container.init_resources()
    container.wire(modules=[__name__])
    return container


container = create_container()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def index():
    return {"message": "hello world"}


@app.post("/bot_request")
@inject
def speech_to_text(
    audio_file: UploadFile = File(...),
    chat_bot_service: ChatBotService = Depends(Provide[Container.chat_bot_service]),
):
    text = chat_bot_service.get_chat_response(audio_file)

    return {"text": text}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
