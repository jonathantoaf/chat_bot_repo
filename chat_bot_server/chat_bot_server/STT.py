import soundfile as sf
from google.cloud import speech_v1p1beta1 as speech
import base64

# Initialize the Google Cloud Speech client using the provided service account key
client = speech.SpeechClient.from_service_account_file("chat_bot_server\key.json")

# Reading the WAV file, gets data and sample rate
data, sample_rate = sf.read("chat_bot_server/14-208-0000.wav")

# Check if the data type is not 'int16', convert it to 'int16'
if data.dtype != 'int16':
    data = (data * 32767).astype('int16')

# Convert the audio data to bytes for API consumption
new_data = data.tobytes()


# Create a RecognitionAudio instance with the audio content
audio_file = speech.RecognitionAudio(content=new_data)

# Configure the speech recognition request
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz = sample_rate, 
    enable_automatic_punctuation = True, 
    language_code = 'en-US'
    )

# Make the speech recognition request to the Google Cloud Speech API
response = client.recognize(
    config = config, 
    audio = audio_file
    )

# Print the result
print(response)
