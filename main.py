from machine import Pin
from utime import sleep_ms, ticks_ms
from random import randint

greenLEDPin = Pin(14, Pin.OUT)
redLEDPin = Pin(15, Pin.OUT)
buttonPin = Pin(16, Pin.IN, Pin.PULL_DOWN)

LEDs = [greenLEDPin, redLEDPin]


IsButtonPressed = False
buttonDebounceTime = 0

def handleButtonPress(pin):
    global IsButtonPressed, buttonDebounceTime
    if (ticks_ms() - buttonDebounceTime > 500):
        IsButtonPressed = True
        buttonDebounceTime = ticks_ms()

buttonPin.irq(trigger=Pin.IRQ_RISING, handler=handleButtonPress)

def toggleLEDs(LEDs: list, delayVal_ms: int, n: int, finalState: int):
    for i in range(n):
        for LED in LEDs:
            LED.on()
            sleep_ms(delayVal_ms)
            LED.off()
            sleep_ms(delayVal_ms)

    for LED in LEDs:
        if(finalState == 1):
            LED.on()
        else:
            LED.off()

def getRandomLED(LEDs: list):
    return LEDs[randint(0, len(LEDs) - 1)]

while True:

    if IsButtonPressed:
        toggleLEDs(LEDs, 90, 5, 0)
        IsButtonPressed = False

        randomLED = getRandomLED(LEDs)
        randomLED.on()
        sleep_ms(1500)
        toggleLEDs([randomLED], 150, 4, 1)
        sleep_ms(1500)
        randomLED.off()
        

