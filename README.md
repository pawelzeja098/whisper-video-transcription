# **Testing OpenAI Whisper for Video Transcription**

## **Project Overview**
This project demonstrates how to use OpenAI's Whisper model to transcribe audio from video files into text. The workflow involves extracting audio from video using tools like `ffmpeg` and then leveraging Whisper's capabilities to generate transcriptions.


## **Getting Started**

### **Prerequisites**
Make sure you have the following installed on your system:
- **Python**: `3.8` - `3.11`
- **ffmpeg**: Required for audio extraction from video files  
  - On **Windows**, example to add `ffmpeg/bin` to your system's PATH in VSC :
    ```powershell
    $env:PATH += ";D:\ffmpeg\bin"
    ```
  - On **Linux**, set the `LD_LIBRARY_PATH` to include the necessary libraries in VSC:
    ```bash
    export LD_LIBRARY_PATH=/lib/x86_64-linux-gnu:/usr/lib/x86_64-linux-gnu
    ```

### **Dependencies**
The project requires the following Python packages:
- **Whisper**: `20240930` (latest release at the time of writing)
- **MoviePy**: `1.0.3`
- **Pydub**: `0.25.1`
- **NumPy**: `2.0.2`
- **PyTorch**: `2.5.1`

You can install all dependencies using the following command:
```bash
pip install openai-whisper moviepy pydub numpy
