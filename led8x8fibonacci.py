#!/usr/bin/python3
""" Manage and display the fibonacci series as a 64 bit integer on an Adafruit LED 8x8 backpack """

import time
from threading import Thread

from Adafruit_Python_LED_Backpack.Adafruit_LED_Backpack import BicolorMatrix8x8

BRIGHTNESS = 5

UPDATE_RATE_SECONDS = 0.2

LARGEST_64_BIT_FIBONACCI = 7540113804746346429

class Led8x8Fibonacci:
    """ Fibinocci diplay on an 8x8 matrix. Represents 1 to largest 64 bit fibinocci number """

    def __init__(self, matrix8x8, lock):
        """ create the fibinacci object """
        self.matrix = matrix8x8
        self.bus_lock = lock
        self.iterations = 0
        self.fib1 = 1
        self.fib2 = 1
        self.fib3 = 2

    def reset(self,):
        """ initialize to starting state and set brightness """
        self.bus_lock.acquire(True)
        self.iterations = 0
        self.fib1 = 1
        self.fib2 = 1
        self.fib3 = 2
        self.matrix.set_brightness(BRIGHTNESS)
        self.bus_lock.release()

    def display(self,):
        """ display the fibinocci series as a 64 bit image """
        time.sleep(UPDATE_RATE_SECONDS)
        self.bus_lock.acquire(True)
        for ypixel in range(0, 8):
            for xpixel in range(0, 8):
                self.iterations += 1
                if self.iterations >= 4:
                    self.iterations = 1
                reg = self.fib3 >> (8 * xpixel)
                bit = reg & (1 << ypixel)
                if bit == 0:
                    self.matrix.set_pixel(ypixel, xpixel, 0)
                else:
                    self.matrix.set_pixel(ypixel, xpixel, self.iterations)
        self.matrix.write_display()
        self.fib1 = self.fib2
        self.fib2 = self.fib3
        self.fib3 = self.fib1 + self.fib2
        if self.fib3 > LARGEST_64_BIT_FIBONACCI:
            self.fib1 = 1
            self.fib2 = 1
            self.fib3 = 2
        self.bus_lock.release()

if __name__ == '__main__':
    exit()
