#!/usr/bin/python3
""" Example of the Fibonacci 8x8 LED matrix dispplay class """

import threading

from Adafruit_Python_LED_Backpack.Adafruit_LED_Backpack import BicolorMatrix8x8

import led8x8fibonacci

if __name__ == '__main__':
    LOCK = threading.Lock.Lock()
    DISPLAY = BicolorMatrix8x8()
    FIB = led8x8fibonacci.Led8x8Fibonacci(MATRIX, LOCK)
    FIB.reset()
    while True:
    	FIB.display()

