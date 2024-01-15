from google.cloud import speech_v1p1beta1 as speech
import os
import os, ssl


if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context


def authenticate_google_cloud():
    """
    Authenticate the application using the Google Cloud credentials.

    Returns:
        None
    """
    keyfile_path = '/Users/jonathan/Documents/GitHub/chat_bot_repo/chat_bot_server/keys/qualified-root-410910-33c1b0c0a7f4.json'
    
    # Set the environment variable for Google Cloud credentials
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = keyfile_path

def speech_to_text(audio_file_path, language_code='en-US'):
    """
    Transcribes speech from an audio file using Google Cloud Speech-to-Text API.

    Args:
        audio_file_path (str): Path to the audio file.
        language_code (str): Language code of the audio (default is 'en-US').

    Returns:
        str: Transcribed text.
    """
    # Authenticate using Google Cloud credentials
    authenticate_google_cloud()

    client = speech.SpeechClient()

    with open(audio_file_path, 'rb') as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code=language_code,
    )

    response = client.recognize(config=config, audio=audio)

    transcribed_text = ''
    for result in response.results:
        transcribed_text += result.alternatives[0].transcript

    return transcribed_text

# Example usage
audio_file_path = '/Users/jonathan/Documents/GitHub/chat_bot_repo/chat_bot_server/data/14-208-0001.wav'
transcribed_text = speech_to_text(audio_file_path)
print("Transcribed Text:")
print(transcribed_text)
