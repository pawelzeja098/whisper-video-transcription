import os


os.environ["IMAGEMAGICK_BINARY"] = "E:/ImageMagick-7.1.1-Q16-HDRI/magick.exe"

from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip


video = VideoFileClip('testdzienswira.mp4')



with open("transcription.txt", "r", encoding="utf-8") as f:
    transcription = f.read()

max_line_length = 40  # Maksymalna długość linii
lines = [transcription[i:i+max_line_length] for i in range(0, len(transcription), max_line_length)]
transcription_split = "\n".join(lines)  # Dołącz linie z powrotem do tekstu

text = TextClip(transcription_split, fontsize=24, color='white', bg_color='black', size=(video.w * 0.3, None))


text = text.set_position(("center", "bottom")).set_duration(video.duration)


final_video = CompositeVideoClip([video, text])


final_video.write_videofile("output_with_subtitles.mp4", codec="libx264", audio_codec="aac")

video.close()