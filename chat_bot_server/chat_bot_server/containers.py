from dependency_injector import containers, providers
from dependency_injector.wiring import Provide, inject

from chat_bot_server.clients.file_system_client import FileSystemClient
from chat_bot_server.clients.google_client import googleClient
from chat_bot_server.services.chat_bot_service import ChatBotService
from pathlib import Path

class Container(containers.DeclarativeContainer):

    config = providers.Configuration()

    file_system_client = providers.Singleton(
        FileSystemClient
    )

    google_client = providers.Singleton(
        googleClient,
        file_system_client=file_system_client,
    )

    chat_bot_service = providers.Singleton(
        ChatBotService,
        file_system_client=file_system_client,
        google_client=google_client,
        audio_files_dir=Path("/Users/jonathan/Documents/BarIlan/chat_bot_repo/chat_bot_server/data")
    )
container = Container()
container.init_resources()
print(container.chat_bot_service)