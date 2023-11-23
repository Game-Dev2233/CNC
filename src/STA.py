import serial
# Define the code for sending the light pixels to the arduino
def send_to_serial(locations, port):
    with serial.Serial(port, 9600, timeout=1) as ser:
        for location in locations:
            x, y = location
            message = f"X:{x}Y:{y}\n"
            ser.write(message.encode())