# RainBoy
# this class manages a LED strip and defines some lookups and color modes.
# it started life as an offshoot of RainMan but for fewer LEDs
#
import adafruit_fancyled.adafruit_fancyled as fancy

class RainBoy :
    def __init__( self, strip ) :
        # refer to
        # https://learn.adafruit.com/fancyled-library-for-circuitpython/led-colors
        # across the rainbow
        self.strip = strip

    def color_selected( self, coloff ) :
        coloff = coloff % 1
        hsv = fancy.CHSV( coloff );
        return hsv.pack()

    def show_static( self, coloff ) :
        color = self.color_selected( coloff )
        self.strip.fill( color )
        self.strip.show()

    def show_static_white( self ) :
        if self.strip.bpp == 4 :
            self.strip.fill((255,255,255,255))
        else :
            self.strip.fill((255,255,255))
        self.strip.show()

    def palette_cycle( self, coloff ) :
        for index in range( self.strip.n  ) :
            color = self.color_selected(coloff)
            self.strip[index] = color
        self.strip.show()