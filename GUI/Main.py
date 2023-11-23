# Define Send To Serial
import serial
# Define the code for sending the light pixels to the arduino
def send_to_serial(locations, port):
    with serial.Serial(port, 9600, timeout=1) as ser:
        for location in locations:
            x, y = location
            message = f"X:{x}Y:{y}\n"
            ser.write(message.encode())

import cv2
import numpy as np
def convert(input_path, output_path):
    # Read the image
    img = cv2.imread(input_path)
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Save the result
    cv2.imwrite(output_path, gray)

import cv2
import numpy as np

def AImage(input_path):
    img = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)  # Read the image in grayscale
    height, width = img.shape  # Get image dimensions
    light_pixel_locations = []  # Initialize an array to store the locations of light pixels
    threshold = 128  # Define a threshold to determine darkness or lightness

    for y in range(height):
        for x in range(width):
            pixel_value = img[y, x]

            # Check if the pixel is light (above the threshold)
            if pixel_value > threshold:
                light_pixel_locations.append((x, y))  # Save the location of the light pixel

    return light_pixel_locations

def start(ardCOM):
    # start the CTC process
    print("Converting Image to Grayscale")
    
    # Convert to grayscale
    convert("image/example.png", "output/exampleout.png")
    
    # declare the array of light pixels
    print("Finding all light pixels in output image")
    light_pixel = AImage("output/exampleout.png")
    print("Sending Data to Arduino")
    
    # send data over serial to Arduino
    send_to_serial(light_pixel, ardCOM)
start('COM6')