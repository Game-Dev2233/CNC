## Overview
Welcome to the CNC Project! This project utilizes a Raspberry Pi, Arduino, and 65C02 to create a CNC machine with robust error detection. The system ensures precise cutting and provides detailed error reports in case of issues.
## Requirements
- Raspberry Pi with a couple of wires
- Arduino board
- 65C02 microprocessor (optional for extra error checking)
- Motors and a knife for the cutting (optional when just doing error checking)
- OpenCV for the raspberry pi
- Arduino IDE for code development (or visual studio code and arduino CLI tools)
## Installation
1. Clone the repository to your Raspberry Pi:

   ```bash
   git clone https://github.com/Game-Dev2233/CNC.git
   ```
2. Upload the Arduino code (`CNC.ino`) to your Arduino board using the Arduino IDE (or CLI).
3. Install required Python libraries on your Raspberry Pi:
   ```bash
   pip install -r requirements.txt
   ```
## Usage

1. Connect the Raspberry Pi, Arduino, 65C02, and CNC hardware according to your setup.

2. Run the main Python script on your Raspberry Pi:

   ```bash
   python cnc_main.py
   ```

3. Follow the on-screen instructions to initiate the CNC process.

## Example Code
### Raspi main script
```python
# import the library to convert the image into a usable format that should work with the arduino and 65c02 (65C02 optional).
import CTC
# start the CTC process
CTC.convert()
```
## Contribution
Feel free to contribute to this project by submitting issues or pull requests.
