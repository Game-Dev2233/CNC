import cv2
import numpy as np
# Defined convert
def convert(input_path, output_path):
    # Read the image
    img = cv2.imread(input_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Save the result
    cv2.imwrite(output_path, gray)