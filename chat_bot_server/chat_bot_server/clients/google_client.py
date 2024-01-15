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

    def speech_to_text(self, audio_file_path: Path) -> str:
        audio_data, sample_rate = self.file_system_client.open_audio_file(audio_file_path)
        audio_data_bytes = audio_data.tobytes()
        client = speech.SpeechClient()
        audio = speech.RecognitionAudio(content=audio_data_bytes)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=sample_rate,
            enable_automatic_punctuation = True,
            language_code="en-US",)
        response = client.recognize(config=config, audio=audio)

        transcribed_text = "f"
        for result in response.results:
            transcribed_text += result.alternatives[0].transcript
        self.__logger.info(f"Transcribed text: {transcribed_text}")
        return transcribed_text

    def translate(self, text_to_translate: str,text_language: str, target_language: str) -> str:
        pass
