from google.cloud import translate_v2
import html

# Set up credentials using the path to your JSON key file
translate_client = translate_v2.Client.from_service_account_json("key.json")

# transalte from a text file
text_file = "text.txt"
with open(text_file, 'r', encoding='utf-8') as file:
    text_to_translate = file.read()

target_language = 'en-US'
result = translate_client.translate(text_to_translate, target_language=target_language)

# Taking only the final translate from the dictionary
final_translate = list(result.values())[0]

# Fixing the ' problem, encoded form -> real character
final_translate = html.unescape(final_translate)

# Write the translated text to the new file
output_file_path = 'output_translate.txt'
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(final_translate)