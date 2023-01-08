# GPT-3_Voice-Assistant

![OpenAI](https://img.shields.io/badge/API-OpenAi-black)   ![J4F](https://img.shields.io/badge/casual-Just%20For%20Fun-brightgreen)
<br/>
This is just a casual 5 minutes project that apply the state-of-the-art language processing model developed by OpenAI, GPT-3 on a Python based voice assistant.

## Step-by-step
### Prerequisite
Before beginning, it is advisable for you to create a virtual environment on your device with tools like [Anaconda](https://www.anaconda.com/).

### 1. Creating an anaconda environment
```
conda env create -f environment.yml
```

### 2. Activate the environment
```
conda activate GPT3_VA
```

### 3. Install speech libraries
This library allows the program to perform speech recognition, with support for several engines and APIs, online and offline
```
pip install SpeechRecognition
```
This library allows the program to perform text-to-speech conversion library in Python.
```
pip install pyttsx3
```

IF you're on Linux machine, please also install this Multi-lingual software speech synthesizer
```
sudo apt-get install libespeak-dev
```
### 4. Obtain GPT-3 API KEY
Sign up and Login to your OpenAI account.
<br/>
<img src="https://github.com/wen-da-ng/GPT-3_voice-assistant/blob/main/.images/Login_page.jpg?raw=true" width=15% height=15%>
<br/>
Once Login, view your API keys on the top right corner.
<br/>
<img src="https://github.com/wen-da-ng/GPT-3_voice-assistant/blob/main/.images/API.jpg?raw=true" width=50% height=50%>
<br/>
Create a new API key if you haven't already
<br/>
<img src="https://github.com/wen-da-ng/GPT-3_voice-assistant/blob/main/.images/Create_API.jpg?raw=true" width=50% height=50%>
<br/>
Copy the API key
<br/>
<img src="https://github.com/wen-da-ng/GPT-3_voice-assistant/blob/main/.images/Copy_API.jpg?raw=true" width=50% height=50%>
<br/>
Paste the API key in the GPT3_VA.py file
<br/>
<img src="https://github.com/wen-da-ng/GPT-3_voice-assistant/blob/main/.images/Paste.jpg?raw=true" width=50% height=50%>
<br/>

### 5. Run the program
```
python3 GPT3_VA.py
```
