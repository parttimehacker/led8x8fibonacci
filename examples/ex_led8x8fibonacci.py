#!/usr/bin/python3
""" Test Bed for Diyhas System Status class """

import time
from threading import Thread, Lock

from Adafruit_Python_LED_Backpack.Adafruit_LED_Backpack import BicolorMatrix8x8

import led8x8fibonacci

if __name__ == '__main__':
    LOCK = Lock()
    DISPLAY = BicolorMatrix8x8()
    FIB = led8x8fibonacci.LedMatrix8x8(MATRIX, LOCK)
    FIB.reset()
    while True:
    	FIB.display()

