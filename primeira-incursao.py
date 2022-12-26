import os
import openai

import azure.cognitiveservices.speech as speechsdk

def recognize_from_mic():
	#Find your key and resource region under the 'Keys and Endpoint' tab in your Speech resource in Azure Portal
	#Remember to delete the brackets <> when pasting your key and region!
    speech_config = speechsdk.SpeechConfig(subscription=os.getenv("TOKEN_GPT"), region="eastus")
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
    
    #Asks user for mic input and prints transcription result on screen
    print("Fale no seu microphone.")
    result = speech_recognizer.recognize_once_async().get()
    print(result.text)
    return result.text

recognize_from_mic()

openai.api_key = os.getenv("TOKEN_GPT")
retorno = openai.Completion.create(
  model="text-davinci-003",
  prompt=recognize_from_mic(),
  max_tokens=22,
  temperature=0
)
texto = retorno["choices"][0]["text"]

texto_sanitizado= texto.replace("\n", "")
print(texto)
with open('/home/carlinhoshk/dev/ressonancia-de-broca/dados_de_saida/arquivos.txt', 'a') as f:
  f.write(str(texto) + "\n")
exit()
