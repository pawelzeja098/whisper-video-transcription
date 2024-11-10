import whisper
import numpy as np
from pydub import AudioSegment
import torch

# Load the mp3 file
audio = AudioSegment.from_mp3("A2.mp3")

# Define start and end times in milliseconds
start_time = 73 * 1000   
end_time = 103 * 1000    

# Trim the audio
trimmed_audio = audio[start_time:end_time]

trimmed_audio = trimmed_audio.set_frame_rate(16000).set_channels(1)

# Convert to numpy array and normalize audio data to be between -1.0 and 1.0
samples = np.array(trimmed_audio.get_array_of_samples()).astype(np.float32) / 32768.0

model = whisper.load_model("large")
result = model.transcribe(samples)

with open("transcription.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])

print(result["text"])


