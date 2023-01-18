import openai
import requests
from gtts import gTTS
import speech_recognition as sr
from playsound import playsound


openai.api_key = "YOUR_API_KEY"

def speak_text(text):
    tts = gTTS(text)
    tts.save("response.mp3")
    playsound("response.mp3")

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = r.listen(source)
    try:
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        return "I'm sorry, I didn't understand that."
    except sr.RequestError:
        return "I'm sorry, I am unable to process your request at this time."

def voice_assistant():
    while True:
        speech_input = listen()
        if speech_input.lower() == "exit":
            break
        else:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=speech_input,
                temperature=0.9, 
                n = 1,
                max_tokens=1024,
                top_p=1.0,
                frequency_penalty=1.0,
                presence_penalty=1.0
            )
            print("You said: {}".format(speech_input))
            response_text = response["choices"][0]["text"]
            print("Assistant: ", response_text)
            speak_text(response_text)

voice_assistant()

