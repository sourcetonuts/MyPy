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

```
import board
import touchio
inputMode = touchio.TouchIn( board.A0 )
```

#### Create a TouchMode

This is how to create an instance of TouchMode.

```
# this will create TouchMode object w/ 3 states: 0, 1, & 2
import MyPy.touchmode
modeMachine = MyPy.touchmode.TouchMode( inputMode, 3 )
```

#### update() checks for a change in state and returns the state

This will check for a change in state and return that state

```
mode = modeMachine.update()
```

This will force a state change/

```
modeMachine.value = 1
```

### RainMan API:

These 5 lines are supporting to pass a neopixel or other strip input 
into RainMan. 12 Leds Neopixel RGBW in this case.

```
import board
import neopixel
num_pixels = 12
strip = neopixel.NeoPixel( 
    board.D4, num_pixels, brightness = 1.0,
    auto_write = False, pixel_order= neopixel.RGBW )
```

#### Create a RainMan

This is how to create an instance of RainMan.

```
3 this will create a RainMan object
import MyPy.rainman
display = MyPy.rainman.RainMan( strip )
```

This will put a rainbow on the LED strip the passed in offest 
between 0 and 1 will define the 1st LED color with the rest of 
strip the rainbow from there.

#### palette_cycle() will put a rainbow on your LED strip

```
display.palette_cycle( offset )
```

#### show_static() will put a color on all LEDs in your LED strip

This will make all LEDs the static color at offset 0 - 1.

```
display.show_static( offset )
```

#### show_static_white() will make all LEDs white

This will make all LEDs white.

```
display.show_static_white()
```
