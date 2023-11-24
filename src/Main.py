import CTC
import PixelA
import STA
import sys
import usage
switch1 = sys.argv[1]
switch2 = sys.argv[2]
def start(ardCOM, ImageInput):
    # start the CTC process
    print("Converting Image to Grayscale")
    
    # Convert to grayscale
    CTC.convert(ImageInput, "output/output.png")
    
    # declare the array of light pixels
    print("Finding all light pixels in output image")
    light_pixel = PixelA.AImage("output/output.png")
    print("Sending Data to Arduino")
    
    # send data over serial to Arduino
    STA.send_to_serial(light_pixel, ardCOM)
start(switch1, switch2)