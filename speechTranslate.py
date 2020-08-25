url = "https://api.eu-de.text-to-speech.watson.cloud.ibm.com/text-to-speech/api"
api = 'ex6tPxJ0Z2OksHtO3Lt6bxzn7gPSeuFBj3yBeNc-j1TJ'

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator(api)
language_translator = LanguageTranslatorV3(
    version='2020-08-25',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-east.language-translator.watson.cloud.ibm.com')
language_translator.set_disable_ssl_verification(True)

from ibm_watson import ApiException
try:
    translation = language_translator.translate(
    text='Hello, how are you today?',
    model_id='en-es').get_result()
    print(json.dumps(translation, indent=2, ensure_ascii=False))
except ApiException as ex:
    print("Method failed with status code " + str(ex.code) + ": " + ex.message)
