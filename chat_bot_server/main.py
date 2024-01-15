import uvicorn
from fastapi import FastAPI, UploadFile
from chat_bot_server.data_models.google_cloud import SpeechToTextResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=False,
        allow_methods=["*"],
        allow_headers=["*"],
    )

@app.get("/")
def index():
    return {"message": "hello world"}


@app.post("/stt", response_model=SpeechToTextResponse)
def speech_to_text(audio_file: UploadFile) -> SpeechToTextResponse:
    return SpeechToTextResponse(text_file_path="path")


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
