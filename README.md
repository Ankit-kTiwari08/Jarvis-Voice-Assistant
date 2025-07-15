# JARVIS - Python Voice Assistant 🤖

**Jarvis** is a smart desktop voice assistant built using Python. It listens to voice commands, opens websites, plays music from a predefined library, and fetches top news headlines — all through speech.

## 🧠 Features

- 🎤 Wake word activation: Say **"Jarvis"** to activate
- 🌐 Open websites like Google, YouTube, LinkedIn, Flipkart
- 🎵 Play music using fuzzy-matched voice commands
- 📰 Fetch and speak the latest news headlines (from NewsAPI)
- 🗣️ Speaks responses using a natural voice (David or Zira)

## 🚀 Demo

> _“Say ‘Jarvis’ to activate...”_

Jarvis: _"Yes?"_  
You: _"Play Khairiyat"_  
Jarvis: _"Playing closest match: Khairiyat..."_

## 🛠️ Tech Stack

- Python 3.x
- `speech_recognition` – for voice input
- `pyttsx3` – for text-to-speech
- `webbrowser` – to open URLs
- `requests` – for API calls
- `difflib` – fuzzy matching for songs

## 🧾 Requirements

Install dependencies:

```bash
pip install -r requirements.txt

📁 Project Structure
css
Copy
Edit
Jarvis-Voice-Assistant/
├── main.py                  # Main assistant code
├── musicLibrary.py          # Dictionary of song names & YouTube links
├── README.md
├── requirements.txt
└── .gitignore
📌 How to Run
bash
Copy
Edit
python main.py
Then speak: "Jarvis" → Followed by your command.

📰 Example Voice Commands
Say This...	What Jarvis Does
"Jarvis"	Activates the assistant
"Open Google"	Opens google.com
"Play Perfect"	Plays the song “Perfect”
"Tell some news"	Reads top 10 headlines

📚 API Used
NewsAPI.org – to fetch headlines
👉 https://newsapi.org

👨‍💻 Author
Developed by Ankit-kTiwari08


