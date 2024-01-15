from typing import Dict, Any
from chat_bot_server.clients.file_system_client import FileSystemClient
import logging
from pathlib import Path
from google.cloud import speech_v1p1beta1 as speech

class GoogleClient:
    def __init__(
        self, config: Dict[str, Any], file_system_client: FileSystemClient
    ) -> None:
        self.__logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        self.file_system_client = file_system_client
        self.api_key = config["api_key"]

    def speech_to_text(self, audio_file_path: Path) -> str:
        audio_data, sample_rate = self.file_system_client.open_audio_file(audio_file_path)
        
        return ""

    def text_to_speech(self, text: str):
        pass
