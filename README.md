### What is this?

- A simple Python application with a simple GUI to generate sound samples to recognize music and display the lyrics of it

### Used 3rd party libraries

- [PyAudio](https://people.csail.mit.edu/hubert/pyaudio/) - Recording and processing audio samples
- [ACRCloud API](https://www.acrcloud.com) - Music Recognition
- [Genius API](https://genius.com/) - Get lyrics by song title

### Installation

**Prerequisites**: Python 3.x with the 3rd party libraries installed

**This installation guide is for Windows only!**
_Tested operation systems:_ Win10

1. Make a local **copy of the repository**.
2. Install **third party libraries**:
   ```python
   pip install pyacrcloud
   pip install lyricsgenius
   pip install pyaudio
   ```

   This didnt really worked for me, so the solution was:
   
   ```python
   #run cmd as administrator
   pip install pipwin
   pipwin install pyaudio
   ```

3. After you installed the dependencies, you have to **create API keys** for ACRCloud and Genius Lyrics:

   - Register, then generate a 14 days free trial _ACRCloud_ key at [this site](https://console.acrcloud.com/avr/projects/online?region=eu-west-1#/projects/online)
   - Do the same with the completely free _Genius API_ [here](https://genius.com/api-clients)
   - Save the keys in a temporary txt file

4. Now lets enable the **Windows Stereo Mixer**:
   You can follow [this short guide](https://www.howtogeek.com/howto/39532/how-to-enable-stereo-mix-in-windows-7-to-record-audio/) to enable the Stereo Mixer in your system.
   **Why?** This will create a virtual input device which can be used to record the samples.

5. Edit the **config.json** file as needed:

   - **ACR_CONFIG**: ACRCloud host and keys
   - **LYRICS_CONFIG**: token of the Genius API
   - **VIDEO_CONFIG**: the first 4 entries is the standard settings of Stereo Mixer and you can change the last two as you like.

6. Done! You can start the program with the following commands:

```
python main.py
```

If you have any **questions or suggestions** about the application contact me via Discord: **SGeri#0731**### What is this?

- A simple Python application with a simple GUI to generate sound samples to recognize music and display the lyrics of it

### Used 3rd party libraries

- [PyAudio](https://people.csail.mit.edu/hubert/pyaudio/) - Recording and processing audio samples
- [ACRCloud API](https://www.acrcloud.com) - Music Recognition
- [Genius API](https://genius.com/) - Get lyrics by song title

### Installation

**Prerequisites**: Python 3.x with the 3rd party libraries installed

**This installation guide is for Windows only!**
_Tested operation systems:_ Win10

1. Make a local **copy of the repository**.
2. Install **third party libraries**:

   ```python
   pip install pyacrcloud
   pip install lyricsgenius
   pip install pyaudio
   ```

   This didnt really worked for me, so the solution was:

   ```python
   #run cmd as administrator
   pip install pipwin
   pipwin install pyaudio
   ```

3. After you installed the dependencies, you have to **create API keys** for ACRCloud and Genius Lyrics:

   - Register, then generate a 14 days free trial _ACRCloud_ key at [this site](https://console.acrcloud.com/avr/projects/online?region=eu-west-1#/projects/online)
   - Do the same with the completely free _Genius API_ [here](https://genius.com/api-clients)
   - Save the keys in a temporary txt file

4. Now lets enable the **Windows Stereo Mixer**:
   You can follow [this short guide](https://www.howtogeek.com/howto/39532/how-to-enable-stereo-mix-in-windows-7-to-record-audio/) to enable the Stereo Mixer in your system.
   **Why?** This will create a virtual input device which can be used to record the samples.

5. Edit the **config.json** file as needed:

   - **ACR_CONFIG**: ACRCloud host and keys
   - **LYRICS_CONFIG**: token of the Genius API
   - **VIDEO_CONFIG**: the first 4 entries is the standard settings of Stereo Mixer and you can change the last two as you like.

6. Done! You can start the program with the following commands:

```
python main.py
```

If you have any **questions or suggestions** about the application contact me via Discord: **SGeri#0731**
