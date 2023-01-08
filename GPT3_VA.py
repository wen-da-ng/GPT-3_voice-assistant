import openai
import speech_recognition as sr
import pyttsx3

openai.api_key = "YOUR_API_KEY"

def generate_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = completions.choices[0].text
    return message

r = sr.Recognizer()

engine = pyttsx3.init()

while True:
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You said: {}".format(text))

        response = generate_response(text)
        print("AI: {}".format(response))

        engine.say(response)
        engine.runAndWait()
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
    except sr.RequestError as e:
        print("Error requesting results from Google Speech Recognition service; {0}".format(e))
