from pydantic import BaseModel, Field

class speechToTextResponse(BaseModel):
    text: str = Field(description="text")


class translateRequest(BaseModel):
    text: str = Field(description="text")
    text_language: str = Field(description="text_language")
    target_language: str = Field(description="target_language")
    
class translateResponse(BaseModel):
    text: str = Field(description="text")

class textToSpeechRequest(BaseModel):
    text: str = Field(description="text")
    language: str = Field(description="language")
    voice: str = Field(description="voice")
