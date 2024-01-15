from pydantic import BaseModel, Field


class SpeechToTextResponse(BaseModel):
    text_file_path: str = Field(description="the path to file that contain the text")

    
