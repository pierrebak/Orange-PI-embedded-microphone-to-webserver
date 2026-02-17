# Orange Pi Embedded Microphone to Webserver

A lightweight solution to stream or record audio from the onboard microphone of an Orange Pi PC (Allwinner H3) directly to a web browser.

---

## 🛠 Prerequisites & Installation

To run this project, you need to install audio management tools (ALSA), the multimedia encoder (FFmpeg), and the Python web framework (Flask).

### 1. Update your system
```bash
sudo apt update
```

### 2. Install Audio and Streaming tools
```bash
sudo apt install -y alsa-utils sox libsox-fmt-all ffmpeg
```

- **alsa-utils**: Controls the onboard microphone.
- **sox**: Useful for local recording tests.
- **libsox-fmt-all**: Extends sox with additional audio formats.
- **ffmpeg**: Handles the real-time audio encoding for the web.

### 3. Install Web Server (Flask)
```bash
sudo apt install -y python3-flask
```

---

## 🎤 Hardware Configuration

Before launching the server, you must configure the microphone permissions and gain levels.

### 1. Join the audio group:
```bash
sudo usermod -aG audio $USER
```

### 2. Adjust the gain:
To prevent background noise and the Larsen effect, set the gain to 60%:
```bash
amixer sset 'Mic1' 60%
```

### 3. Save settings:
To ensure settings persist after a reboot:
```bash
sudo alsactl store
```

---

## 🚀 How to use

### 1. Clone the repository:
```bash
git clone https://github.com/pierrebak/Orange-PI-embedded-microphone-to-webserver.git
cd Orange-PI-embedded-microphone-to-webserver
```

### 2. Run the server:
```bash
python3 opimic2webserver.py
```

### 3. Access the interface:
Open your browser and enter your Orange Pi's IP address on port 5001:
```
http://192.168.1.xxx:5001
```

---

## ⚠️ Important Notes

- **Larsen Effect**: If you hear a loud feedback loop, use headphones or move the Orange Pi away from your speakers.
- **Latency**: A delay of 2-3 seconds is expected due to network buffering and encoding.
- **Network**: Ensure both devices are on the same local network.
