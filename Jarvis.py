import speech_recognition as sr
import webbrowser
import pyttsx3
import time
import musicLibrary  #made library
import difflib #fuzzy matching
import requests


recognizer = sr.Recognizer()
engine = pyttsx3.init()

newsapi = "your api key"

def speak(text):
    try:
        time.sleep(0.3)
        engine = pyttsx3.init('sapi5')  # Use 'sapi5' for Windows,
        engine.say(text)
        engine.runAndWait()
        engine.stop()
    except Exception as e:
        print("Speech error:", e)

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("http://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("http://youtube.com") 
    elif "open linkedin" in c.lower():
        webbrowser.open("http://linkedin.com") 
    elif "open flipkart" in c.lower():
        webbrowser.open("http://flipkart.com") 
    elif c.startswith("play"):
        song_input = c.replace("play", "").strip().replace(" ", "")
        print(f"You said: '{song_input}'")

        # Get closest match from music library
        possible_matches = difflib.get_close_matches(song_input, musicLibrary.music.keys(), n=1, cutoff=0.5)

        if possible_matches:
            song_key = possible_matches[0]
            print(f"Playing closest match: {song_key}")
            webbrowser.open(musicLibrary.music[song_key])
        else:
            speak("Sorry, I couldn't find a matching song.")
            print("No close match found.")

    elif "news" in c.lower():
        r= requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200: 
            data = r.json()
            
            #extract data's
            articles = data.get("articles", [])
    
            #print headlines
            for article in articles:
                speak(article['title'])
                
                    



if __name__== "__main__":
    speak("Initializing Jarvis....")
    while True:
        r = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("Say 'Jarvis' to activate...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)
                word = recognizer.recognize_google(audio)

                if word.lower() == "jarvis":
                    print("Jarvis Activated")
                    speak("Yes")

                    print("Listening for command...")
                    audio = recognizer.listen(source, timeout=5)
                    command = recognizer.recognize_google(audio)
                    print("Command:", command)
                    
                    
                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))