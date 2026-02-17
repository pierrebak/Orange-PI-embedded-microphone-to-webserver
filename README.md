
<img width="1901" height="960" alt="image" src="https://github.com/user-attachments/assets/2f733fff-d368-426b-8a05-82dac1483ec6" />


To run this project, you need to install the audio management tools (ALSA), the multimedia encoder (FFmpeg), and the Python web framework (Flask).
1. Update your system

Ensure your package list is up to date to avoid "404 Not Found" errors during installation:
Bash

sudo apt update

2. Install Audio and Streaming tools

These packages allow the Orange Pi to capture audio from the hardware and process it for the web:
Bash

sudo apt install -y alsa-utils sox libsox-fmt-all ffmpeg

    alsa-utils: Provides arecord and amixer to control the onboard microphone.

    sox: A powerful audio manipulation tool used for recording tests.

    ffmpeg: The engine used to stream the audio live to your browser.

3. Install Web Server (Flask)

We use Flask to create the web interface:
Bash

sudo apt install -y python3-flask

🎤 Hardware Configuration

Before launching the server, you must enable the microphone and set the gain level.

    Join the audio group (if not already done):
    Bash

    sudo usermod -aG audio $USER

    Adjust the gain:
    To avoid the Larsen effect (feedback) and background noise, set the microphone gain to 50% or 60%:
    Bash

    amixer sset 'Mic1' 60%

    Save settings:
    To keep these settings after a reboot:
    Bash

    sudo alsactl store

🚀 How to use

    Clone the repository:
    Bash

    git clone https://github.com/pierrebak/Orange-PI-embedded-microphone-to-webserver.git
    cd Orange-PI-embedded-microphone-to-webserver

    Run the server:
    Bash

    python3 app.py

    Access the interface:
    Open your browser and type your Orange Pi IP address on port 5001:
    http://192.168.1.xxx:5001
