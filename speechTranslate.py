from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json

url = '' # enter your URL
apikey = '' # enter your API key

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2020-08-25',
    authenticator=authenticator
)

language_translator.set_service_url(url)

langs = {
    "english": "en",
    "french": "fr",
    "german": "de",
    "spanish": "es",
    "hindi": "hi"
}

print("Choose a language to translate from (english, french, german, spanish, hindi): ")
source = input()
print("Choose a language to translate into (english, french, german, spanish, hindi): ")
target = input()
print("Enter a Sentence to be translated")
text = input()

from ibm_watson import ApiException
try:
    translation = language_translator.translate(
    text=text,
    source=source, target=target).get_result()
    print(json.dumps(translation, indent=2, ensure_ascii=False))
except ApiException as ex:
    print("Method failed with status code " + str(ex.code) + ": " + ex.message)
