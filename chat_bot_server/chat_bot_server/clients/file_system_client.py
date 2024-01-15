import logging
from pathlib import Path
from typing import Any, Tuple

import soundfile as sf
from fastapi import UploadFile


class FileSystemClient:
    def __init__(self) -> None:
        self.__logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")

    def save_audio_file(self, audio_file: UploadFile, audio_file_path: Path) -> None:
        try:
            dir_path = audio_file_path.parent
            dir_path.mkdir(parents=True, exist_ok=True)
            with audio_file_path.open("wb") as audio_file_output:
                audio_file_output.write(audio_file.file.read())
            self.__logger.debug(f"File saved successfully at {audio_file_path}")
        except Exception as e:
            self.__logger.error(
                f"An error occurred: {str(e)}. when try to save the audio file in this path :{audio_file_path}"
            )

    def open_audio_file(self, audio_file_path: Path) -> Tuple[Any, int]:
        try:
            data, sample_rate = sf.read(audio_file_path)
            self.__logger.debug(f"Audio file {audio_file_path} opened successfully")
            return data, sample_rate
        except Exception as e:
            self.__logger.error(
                f"An error occurred: {str(e)}. when try to open the audio file in this path :{audio_file_path}"
            )
            raise e
