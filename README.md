# Orange Pi Embedded Microphone to Webserver

Welcome to the Orange Pi Embedded Microphone to Webserver project! 🎤🌐 This guide will walk you through the prerequisites, installation steps, hardware configuration, and usage instructions to get your system up and running.

---

## Prerequisites
Before you begin, ensure you have the following installed:
- **Orange Pi** board (any model supported)
- **Microphone** (embedded or external)
- **Network connection** (Wi-Fi or Ethernet)
- **Latest version of Raspbian** or your preferred OS on Orange Pi

## Installation
Follow these steps for a successful installation:
1. **Clone the repository:**  
   Use the following command:
   ```bash
   git clone https://github.com/pierrebak/Orange-PI-embedded-microphone-to-webserver.git
   ```
2. **Navigate to the project directory:**  
   ```bash
   cd Orange-PI-embedded-microphone-to-webserver
   ```
3. **Install dependencies:**  
   Ensure you run:
   ```bash
   sudo apt-get install <dependencies>
   ```
   *(Replace `<dependencies>` with required libraries.)*

## Hardware Configuration
1. **Connect the microphone** to your Orange Pi:
   - Pins: [Specify pin connections]
   (Refer to the Orange Pi pinout diagram for clarity.)

2. **Verify connection:**  
   Use the command:
   ```bash
   aplay -l
   ```
   *(This will list all audio devices. Ensure your microphone appears.)*

## Usage Instructions
Once everything is set up, you can run the server by executing:
```bash
python3 server.py
```

### Accessing the Web Interface
Open your web browser and go to:
```
http://<Orange_Pi_IP>:<port>
```
*Replace `<Orange_Pi_IP>` with your device's IP address and `<port>` with the specified port in your `server.py`.*

---

Enjoy your audio streaming experience! 🎉 If you encounter any issues, please refer to the troubleshooting section or contact the maintainers.