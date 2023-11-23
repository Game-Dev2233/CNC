import CTC
import PixelA
import STA
def start(ardCOM):
    # start the CTC process
    print("Converting Image to Grayscale")
    
    # Convert to grayscale
    CTC.convert("image/example.png", "output/exampleout.png")
    
    # declare the array of light pixels
    print("Finding all light pixels in output image")
    light_pixel = PixelA.AImage("output/exampleout.png")
    print("Sending Data to Arduino")
    
    # send data over serial to Arduino
    STA.send_to_serial(light_pixel, ardCOM)
start('COM6')