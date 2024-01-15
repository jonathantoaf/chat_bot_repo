from pydantic import BaseModel, Field
from typing import ByteString

class ChatBotResponse(BaseModel) :
    audio_bytes: ByteString = Field(description="the path to file that contain the text")

    
