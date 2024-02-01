import logging
from fastapi import UploadFile
from pathlib import Path

from chat_bot_server.clients.file_system_client import fileSystemClient
from chat_bot_server.clients.google_client import googleClient


class chatBotService:
    def __init__(
        self,
        file_system_client: fileSystemClient,
        google_client: googleClient,
        audio_files_dir: Path
    ) -> None:
        self.__logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        self.file_system_client = file_system_client
        self.google_client = google_client
        self.audio_files_dir = audio_files_dir

    def speech_to_text(self, audio_file: UploadFile) -> str:
        audio_file_path = self.audio_files_dir / "input_audio.wav"
        self.file_system_client.save_audio_file(audio_file, audio_file_path)
        input_text = self.google_client.speech_to_text(audio_file_path)
        return input_text

    def translate(self, text: str, text_language: str, target_language: str) -> str:
        translate_text =  self.google_client.translate(text, text_language, target_language)
        return translate_text