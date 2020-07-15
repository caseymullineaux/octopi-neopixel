import time
from rpi_ws281x import PixelStrip, Color
import argparse

LED_COUNT = 6
LED_PIN = 18
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

def flash(count=3, delay=1, color=Color(255,255,255)):
    """Flashes pixels with the color specified"""
    i = 0
    while i < count:
        for pixel in range(strip.numPixels()):
            strip.setPixelColor(pixel, color)
        strip.show()
        time.sleep(delay)

        for pixel in range(strip.numPixels()):
            strip.setPixelColor(pixel, Color(0,0,0))
        strip.show()
        time.sleep(delay)

        i+=1

def colorWipe(color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

def triColorWipe(color):
    """Three color wipes in a row, turning off pixels once completed."""
    colorWipe(color)
    time.sleep(0.1)
    pixelsOff()
    colorWipe(color)
    time.sleep(0.1)
    pixelsOff()
    colorWipe(color)
    time.sleep(0.1)
    pixelsOff()

def pixelsOff():
    """Turns all pixels off"""
    for pixel in range(strip.numPixels()):
        strip.setPixelColor(pixel,Color(0,0,0)) # OFF
    strip.show()

if __name__ == '__main__':
    # process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--event', help='I should probably write something helpful here')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)

    # Intialize the library (must be called once before other functions).
    strip.begin()
    
    if args.event.lower() == 'connected':
        triColorWipe(Color(0,255,0))

    if args.event.lower() == 'disconnected':
        triColorWipe(Color(255,0,0))
        
    if args.event.lower() == 'printstarted':
        flash(color=Color(255,0,255)) # PURPLE
        for pixel in range(strip.numPixels()):
            strip.setPixelColor(pixel,Color(255,255,255)) # WHITE
        strip.show()

    if args.event.lower() == 'printdone':
        flash(count=10,color=Color(0,255,00)) # GREEN
        
    if args.event.lower() == 'printfailed':
        flash(count=10, color=Color(255,0,0))

    if args.event.lower() == 'printpaused':
        for pixel in range(strip.numPixels()):
            strip.setPixelColor(pixel,Color(255,128,0)) # YELLOW
        strip.show()

    if args.event.lower() == 'cooling':
        for pixel in range(strip.numPixels()):
            strip.setPixelColor(pixel,Color(0,0,255)) # BLUE
        strip.show()
        
    if args.event.lower() == 'home':
        for pixel in range(strip.numPixels()):
            strip.setPixelColor(pixel,Color(255,80,0)) # ORANGE/YELLOW
        strip.show()

    if args.event.lower() == 'off':
        for pixel in range(strip.numPixels()):
            strip.setPixelColor(pixel,Color(0,0,0)) # OFF
        strip.show()


