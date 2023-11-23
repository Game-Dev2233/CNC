# import the library to convert the image into a usable format
# that should work with the arduino and 65c02 (65C02 optional).
import CTC
import PixelA
import STA
import json
def start(ardCOM):
    debug = 1
    # start the CTC process
    print("Converting Image to Grayscale")
    # Convert to grayscale
    CTC.convert("image/example.png", "output/exampleout.png")
    print("Finding all light pixels in output image")
    # declare the array of light pixels
    light_pixel = PixelA.AImage("output/exampleout.png")
    print("Sending Data to Arduino")
    # send data to the arduino from COM6
    STA.send_to_serial(light_pixel, ardCOM)
    # print debug information if debug = 1
    if debug=="1":
        print(light_pixel)
start('COM6')