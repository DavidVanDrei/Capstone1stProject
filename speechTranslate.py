from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json

url = ''
apikey = ''

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2020-08-25',
    authenticator=authenticator
)

language_translator.set_service_url(url)

print("Enter a Sentence in English to be translated")
text = input()

from ibm_watson import ApiException
try:
    translation = language_translator.translate(
    text='Hello, how are you today?',
    model_id='en-es').get_result()
    print(json.dumps(translation, indent=2, ensure_ascii=False))
except ApiException as ex:
    print("Method failed with status code " + str(ex.code) + ": " + ex.message)
