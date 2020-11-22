# My Py

Provides the library functions for my Circuit Python efforts

## Usage:

To include in another project, use GIT Submodules
https://git-scm.com/book/en/v2/Git-Tools-Submodules

In your project's source directory:
git submodule add https://github.com/sourcetonuts/MyPy

Which creates a directory MyPy w/ the library and a .gitsubmodules file 
that you need to check in.

## API:

### TouchMode API:

These 3 lines are supporting to pass a CapSense input into TouchMode

<code>
import board
import touchio
inputMode = touchio.TouchIn( board.A0 )
</code>

This is how to create an instance of TouchMode.

<code>
# this will create TouchMode object w/ 3 states: 0, 1, & 2
import MyPy.touchmode
modeMachine = MyPy.touchmode.TouchMode( inputMode, 3 )
</code>

This will check for a change in state and return that state

<code>
mode = modeMachine.update()
</code>

This will force a state change

<code>
modeMachine.value = 1
</code>

### RainMan API:

These 5 lines are supporting to pass a neopixel or other strip input 
into RainMan. 12 Leds Neopixel RGBW in this case.

<code>
import board
import neopixel
num_pixels = 12
strip = neopixel.NeoPixel( 
    board.D4, num_pixels, brightness = 1.0,
    auto_write = False, pixel_order= neopixel.RGBW )
</code>

This is how to create an instance of RainMan.

<code>
3 this will create a RainMan object
import MyPy.rainman
display = MyPy.rainman.RainMan( strip )
</code>

This will put a rainbow on the LED strip the passed in offest 
between 0 and 1 will define the 1st LED color with the rest of 
strip the rainbow from there.

<code>
display.palette_cycle( offset )
</code>

This will make all LEDs the static color at offset 0 - 1.

<code>
display.show_static( offset )
</code>

This will make all LEDs white.

<code>
display.show_static_white()
</code>
