import asyncio
import os
import openai
import azure.cognitiveservices.speech as speechsdk

async def recognize_from_mic():
    speech_config = speechsdk.SpeechConfig(subscription=os.getenv("TOKEN_AZURE"), region="eastus",  speech_recognition_language='pt-br')
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
    
    print("Fale no seu microphone.")
    result = speech_recognizer.recognize_once_async().get()
    print(result.text)
    return result.text

async def call_openai(prompt):
    openai.api_key = os.getenv("TOKEN_GPT")
    retorno = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=22,
        temperature=0
    )
    texto = retorno["choices"][0]["text"]
    print(texto)

async def main():
    # Aguarda o resultado da chamada da função recognize_from_mic
    prompt = await recognize_from_mic()
    # Passa o resultado da chamada da função recognize_from_mic como argumento para a função call_openai
    await call_openai(prompt)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
