## check the available languages
from TTS.api import TTS
model_name = TTS.list_models()[0]
tts = TTS(model_name)
print(f"Available languages: {tts.languages}")

## python3 languages_2.py

## Available languages: ['en', 'es', 'fr', 'de', 'it', 'pt', 'pl', 'tr', 'ru', 'nl', 'cs', 'ar', 'zh-cn', 'hu', 'ko', 'ja', 'hi']

