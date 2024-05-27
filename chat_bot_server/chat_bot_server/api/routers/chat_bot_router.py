from dependency_injector.wiring import inject
from fastapi import APIRouter

from chat_bot_server.services.chat_bot_service import ChatBotService
from fastapi import Depends, File, UploadFile
from dependency_injector.wiring import Provide, inject
from chat_bot_server.containers import Container
from chat_bot_server.data_models.chat_bot import speechToTextResponse, translateRequest, translateResponse


router = APIRouter(prefix="/chat-bot", tags=["chat-bot"])


@router.post(path="/speech-to-text")
@inject
def speech_to_text(
    audio_file: UploadFile = File(...),
    chat_bot_service: ChatBotService = Depends(Provide[Container.chat_bot_service]),
) -> speechToTextResponse:
    text = chat_bot_service.speech_to_text(audio_file)
    return speechToTextResponse(text=text)

@router.post(path="/translate")
@inject
def translate(
    translate_request: translateRequest,
    chat_bot_service: ChatBotService = Depends(Provide[Container.chat_bot_service]),
) -> translateResponse:
    text = chat_bot_service.translate(translate_request.text, translate_request.text_language, translate_request.target_language)
    return translateResponse(text=text)