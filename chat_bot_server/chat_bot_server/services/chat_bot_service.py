import logging
from fastapi import UploadFile
from pathlib import Path

from chat_bot_server.clients.file_system_client import FileSystemClient
from chat_bot_server.clients.google_client import GoogleClient
from chat_bot_server.clients.openai_client import OpenAiClient


class ChatBotService:
    def __init__(
        self,
        file_system_client: FileSystemClient,
        goole_client: GoogleClient,
        openai_client: OpenAiClient,
        audio_files_dir: Path
    ) -> None:
        self.__logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        self.file_system_client = file_system_client
        self.google_client = goole_client
        self.openai_client = openai_client
        self.audio_files_dir = audio_files_dir

    def get_chat_response(self, audio_file: UploadFile):
        audio_file_path = self.audio_files_dir / "input_audio.wav"
        self.file_system_client.save_audio_file(audio_file, audio_file_path)
        input_text = self.google_client.speech_to_text(audio_file_path)
        return input_text
