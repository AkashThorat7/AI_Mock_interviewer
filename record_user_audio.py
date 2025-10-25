import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write

def record_audio(duration=60, filename="response.wav"):
    fs = 16000
    print("🎙️ Recording started. You have 60 seconds to answer...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype="int16")
    sd.wait()
    write(filename, fs, audio)
    print("✅ Recording stopped.")
    return filename
