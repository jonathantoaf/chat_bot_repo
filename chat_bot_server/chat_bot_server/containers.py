from dependency_injector import containers, providers
from dependency_injector.wiring import Provide, inject

from chat_bot_server.clients.file_system_client import FileSystemClient
from chat_bot_server.clients.google_client import GoogleClient
from chat_bot_server.clients.openai_client import OpenAiClient
from chat_bot_server.services.chat_bot_service import ChatBotService

class Container(containers.DeclarativeContainer):

    config = providers.Configuration()

    file_system_client = providers.Singleton(
        FileSystemClient
    )

    google_client = providers.Singleton(
        GoogleClient,
        api_key=config.api_key,
    )

    openai_client = providers.Singleton(
        OpenAiClient,
        api_key=config.api_key,
    )

    service = providers.Factory(
        ChatBotService,
        file_system_client=file_system_client,
        google_client =google_client,
        openai_client = openai_client,
    )