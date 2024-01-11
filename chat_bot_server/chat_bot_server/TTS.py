from google.cloud import texttospeech

def synthesize_text(text, output_file_path, language_code='en-US', voice_name='en-US-Wavenet-D', speaking_rate=1.0):
    # Set up credentials using the path to your JSON key file
    client = texttospeech.TextToSpeechClient.from_service_account_file("key.json")

    # Set the input text and voice parameters
    input_text = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code=language_code,
        name=voice_name,
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16,
        speaking_rate=speaking_rate,
    )

    # Perform the text-to-speech synthesis
    response = client.synthesize_speech(input=input_text, voice=voice, audio_config=audio_config)

    # Save the synthesized audio to a file
    with open(output_file_path, 'wb') as output_file:
        output_file.write(response.audio_content)

# Example usage
text_to_synthesize = "Hello, how are you today?"
output_wav_file = "output.wav"
synthesize_text(text_to_synthesize, output_wav_file)
