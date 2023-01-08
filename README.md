# GPT-3_voice-assistant
This is just a casual 5 minutes project that apply the state-of-the-art language processing model developed by OpenAI on a Python based voice assistant.

## Step-by-step
### Prerequisite
Before beginning, it is advisable for you to create a virtual environment on your device with tools like [Anaconda](https://www.anaconda.com/).

### 1. Creating an anaconda environment
```
conda env create -f environment.yml
```

### 2. Activate the environment
```
conda activate chatGPT_VA
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

### 4. Run the program
```
python3 chatGPT_VA.py
```
