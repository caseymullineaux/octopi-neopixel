import time
from rpi_ws281x import PixelStrip, Color
import argparse
import enum

LED_COUNT = 10
LED_PIN = 18
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

def flash(count=3, delay=1, color=Color(255,255,255)):
    if color is None:
        color = Color(255,255,255)

    i = 0
    while i < count:
        strip.setPixelColor(0, color) # RED
        strip.show()
        time.sleep(delay)
        strip.setPixelColor(0, Color(0,0,0)) # RED
        strip.show()
        time.sleep(delay)
        i+=1

if __name__ == '__main__':
    # process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--event', help='')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)

    # Intialize the library (must be called once before other functions).
    strip.begin()

    if args.event == 'start':
        flash(color=Color(0,255,0)) # GREEN
    if args.event == 'complete':
        flash(count=10,color=Color(255,0,255))
    if args.event == 'heat':
        strip.setPixelColor(0,Color(255,0,0)) # RED
        strip.show()
    if args.event == 'cooldown':
        strip.setPixelColor(0,Color(0,0,255)) # BLUE
        strip.show()
    if args.event == 'print':
        strip.setPixelColor(0,Color(255,255,255)) # WHITE
        strip.show()
    if args.event == 'off':
        strip.setPixelColor(0,Color(0,0,0)) # OFF
        strip.show()


