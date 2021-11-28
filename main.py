# import libraries
from acrcloud.recognizer import ACRCloudRecognizer
from tkinter import *
import tkinter.font as tkFont
import lyricsgenius
import json
import pyaudio
import wave
import threading

# import app settings
with open("config.json", encoding = 'utf-8') as f:
    config = json.load(f)

    ACR_CONFIG = config["ACR_CONFIG"]
    VIDEO_CONFIG = config["VIDEO_CONFIG"]
    LYRICS_CONFIG = config["LYRICS_CONFIG"]

    VIDEO_CONFIG["FORMAT"] = pyaudio.paInt16 # change if needed

# use the devices.py script to detect your stereo mixer 
DEVICE_ID = 20

# pyaudio & geniuslyrics
p = pyaudio.PyAudio()
genius = lyricsgenius.Genius(LYRICS_CONFIG["TOKEN"])

# record sample from audio device
def record_sample():
    stream = p.open(format = VIDEO_CONFIG["FORMAT"], 
                    channels = VIDEO_CONFIG["CHANNELS"], 
                    rate = VIDEO_CONFIG["RATE"], 
                    frames_per_buffer = VIDEO_CONFIG["CHUNK"], 
                    input_device_index = 20,
                    input = True)

    frames = []

    for _ in range(0, int(VIDEO_CONFIG["RATE"] / VIDEO_CONFIG["CHUNK"] * VIDEO_CONFIG["SAMPLE_LENGTH"])):
        data = stream.read(VIDEO_CONFIG["CHUNK"])
        frames.append(data)

    stream.stop_stream()
    stream.close()

    wf = wave.open(VIDEO_CONFIG["TMP_FILE_NAME"], 'wb')
    wf.setnchannels(VIDEO_CONFIG["CHANNELS"])
    wf.setsampwidth(p.get_sample_size(VIDEO_CONFIG["FORMAT"]))
    wf.setframerate(VIDEO_CONFIG["RATE"])
    wf.writeframes(b''.join(frames))
    wf.close()

# recognize song from sample with acrcloud api
def recognize_sample():
    acrcloud = ACRCloudRecognizer(ACR_CONFIG)

    results = acrcloud.recognize_by_file('output.wav', 0)
    results = json.loads(results)

    # 2006: muted; 1001: no result
    print(results["status"]["code"])
    if results["status"]["code"] == 2006 or results["status"]["code"] == 1001:
        return {"success": False, "error": "Recognition failed"}
    else:
        return {"success": True, "name": results["metadata"]["music"][0]["artists"][0]["name"] + ": " + results["metadata"]["music"][0]["title"]} 

# get lyrics by song title with genius api
def get_lyrics_by_title(song):
    search_song = genius.search_song(song)

    if search_song is None:
        long_text["text"] += "\nLyrics not found"
    else:
        long_text["text"] += "\n\n" + search_song.lyrics

# ui handler functions
def start_searching():
    start_button.place_forget()
    title_text["text"] = "Wait for the app to\nfinish the analysis!"
    long_text["text"] = "Recording sample..."

    global record_thread
    record_thread = threading.Thread(target = record_sample)
    record_thread.start()
    root.after(20, check_record_thread)

def check_record_thread():
    if record_thread.is_alive():
        root.after(20, check_record_thread)
    else:
        record_thread.join()

        long_text["text"] = "Sample recorded, recognizing..."
        recognize_results = recognize_sample()

        if recognize_results["success"]:
            long_text["text"] = "Recognized: " + recognize_results["name"]

            get_lyrics_by_title(recognize_results["name"])
        else:
            long_text["text"] = recognize_results["error"]

        start_button.place(x = 200, y = 10, width = 77, height = 40)
        title_text["text"] = "Start the recognizer\nby clicking the button!"

# build ui
root = Tk()
root.title("Music Recognition")
root.geometry("300x800")
root.resizable(width = False, height = False)

title_text = Label(root)
title_text["font"] = tkFont.Font(family = 'Times', size = 12)
title_text["fg"] = "#333333"
title_text["justify"] = "center"
title_text["text"] = "Start the recognizer\nby clicking the button!"
title_text.place(x = 20, y = 10, width = 160, height = 40)

# TODO scrollable text
long_text = Label(root, anchor = NW, wraplength = 270)
long_text["font"] = tkFont.Font(family = 'Times', size = 10)
long_text["fg"] = "#333333"
long_text["justify"] = "center"
long_text.place(x = 20, y = 60, width = 270, height = 300)

start_button = Button(root, bg="grey")
start_button["font"] = tkFont.Font(family = 'Times', size = 18)
start_button["justify"] = "center"
start_button["text"] = "Start"
start_button["command"] = start_searching
start_button.place(x = 200, y = 10, width = 77, height = 40)

root.mainloop()