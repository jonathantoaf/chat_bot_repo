import logging
from pathlib import Path
from typing import Any, Dict

from google.cloud import speech_v1p1beta1 as speech
from google.cloud import translate_v2 as translate

from chat_bot_server.clients.file_system_client import fileSystemClient


class googleClient:
    def __init__(
        self, file_system_client: fileSystemClient
    ) -> None:
        self.__logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        self.file_system_client = file_system_client

    def speech_to_text(self, audio_file_path: Path) -> str:
        audio_file_path = Path("/Users/jonathan/Documents/BarIlan/chat_bot_repo/chat_bot_server/data/input_audio2.wav")
        audio_data, sample_rate = self.file_system_client.open_audio_file(audio_file_path)
        if audio_data.dtype != 'int16':
            audio_data = (audio_data * 32767).astype('int16')
        audio_data_bytes = audio_data.tobytes()
        client = speech.SpeechClient()
        audio = speech.RecognitionAudio(content=audio_data_bytes)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=sample_rate,
            enable_automatic_punctuation = True,
            language_code="en-US",)
        response = client.recognize(config=config, audio=audio)

        transcribed_text = ""
        for result in response.results:
            transcribed_text += result.alternatives[0].transcript
        self.__logger.info(f"Transcribed text: {transcribed_text}")
        return transcribed_text

    def translate(self, text: str,text_language: str, target_language: str) -> str:
        client = translate.Client()
        result = client.translate(text, source_language=text_language, target_language=target_language)
        final_translate = list(result.values())[0]
        return final_translate

