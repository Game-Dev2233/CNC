## Overview
Welcome to the CNC Project! This project utilizes a Raspberry Pi, Arduino, and 65C02 to create a CNC machine with robust error detection. The system ensures precise cutting and provides detailed error reports in case of issues.
## Requirements
- Raspberry Pi with a USB connected to a arduino uno
- Arduino uno
- Motors and a knife for the cutting (optional when just doing error checking)
- Arduino IDE for code development (or your code editor of choice combined with the arduino CLI tools)
## Installation
1. Clone the repository to your Raspberry Pi/Computer:

   ```bash
   git clone https://github.com/Game-Dev2233/CNC.git
   ```
2. Upload the Arduino code (`CNC.ino`) to your Arduino board using the Arduino IDE (or CLI).
3. Install required Python libraries on your Raspberry Pi:
   ```bash
   pip install -r requirements.txt
   ```
## Usage

1. Connect the Raspberry Pi (Or computer), Arduino, 65C02 (Optional), and CNC hardware.

2. Run the main Python script on your Raspberry Pi:

   ```bash
   python src/main.py [COM+PORT NUMBER] [IMAGE LOCATION]
   ```
## Contribution
Feel free to contribute to this project by submitting issues or pull requests.
