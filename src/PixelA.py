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