"""
📄 Project 9: Text to Speech Converter (Offline)
👨‍💻 Created by: Hashir Adnan  
🌐 Website: www.techthf.xyz  
🗓️ Date: [Insert today’s date]

🧠 Description:
This Python script converts any text you enter into speech using your system’s voice engine.
It can also save the voice output to an MP3 file.

📦 Features:
- Offline text-to-speech conversion
- Uses system's default voice
- Option to save audio as an MP3 file
- Fast and lightweight

🧰 Tools & Modules Used:
- pyttsx3: for offline speech synthesis
- os: to handle file saving

💡 How to Use:
1. Install required module: `pip install pyttsx3`
2. Run the script: `python main.py`
3. Enter your text when prompted.
4. The system will speak it aloud and save it as `output.mp3`.

✅ Example:
Input: "Hello, this is Hashir's Python project."  
Output: Voice plays and `output.mp3` is created.
"""

import pyttsx3

def text_to_speech(text, filename="output.mp3"):
    engine = pyttsx3.init()
    engine.save_to_file(text, filename)
    engine.runAndWait()
    print(f"✅ Audio saved as {filename}")

if __name__ == "__main__":
    user_text = input("📝 Enter the text you want to convert to speech:\n> ")
    text_to_speech(user_text)
