import uvicorn
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pathlib import Path

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


@app.post("/bot_request")
def speech_to_text(audio_file: UploadFile = File(...)) -> StreamingResponse:
    audio_file_path = Path("/Users/jonathan/Documents/GitHub/chat_bot_repo/chat_bot_server/data/file.wav")
    with audio_file_path.open("wb") as audio_file_output:
                audio_file_output.write(audio_file.file.read())
    def iterfile():
        with open(str(audio_file_path), 'rb') as audio_file_2:
            while True:
                chunk = audio_file_2.read(1024)
                if not chunk:
                    break
                yield chunk
    return StreamingResponse(iterfile(), media_type="application/octet-stream")
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
a