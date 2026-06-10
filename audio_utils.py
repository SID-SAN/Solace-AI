import tempfile
import speech_recognition as sr
from gtts import gTTS

def transcribe_audio(audio_path):

    if not audio_path:
        return ""
        
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(audio_path) as source:
            audio_data = recognizer.record(source)
            return recognizer.recognize_google(audio_data)
    except sr.UnknownValueError:
        return "(Sorry, I couldn't understand that.)"
    except sr.RequestError:
        return "(Speech recognition service is unavailable.)"
    except Exception as e:
        return f"(Audio processing error: {str(e)})"

def generate_voice(text):

    if not text:
        return None

    reply_lines = [line.strip() for line in text.split("\n") if line.strip()]
    final_reply = reply_lines[-1] if reply_lines else "(No response generated.)"

    try:
        tts = gTTS(final_reply, lang="en", tld="co.in")
        
        temp_audio_path = tempfile.mktemp(suffix=".mp3")
        tts.save(temp_audio_path)
        return temp_audio_path
    except Exception as e:
        print(f"TTS Generation failed: {str(e)}")
        return None