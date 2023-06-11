import pyttsx3
engine = pyttsx3.init()
text = "Welcome to python programming"
engine.say(text)
engine.runAndWait()