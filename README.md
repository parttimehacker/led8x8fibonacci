led8x8fibonacci
=====
Displays the fibonacci sequence as a 64 bit value on an Adafruit 8x8 matrix LED backpack. Each bit of a long long (64 bit integer) is tested and displayed. Zeros are black and ones are colored. The color is rolled from green, yellow and red in sequence.

Requirements
```
8x8 LED device and a thread lock passed during Led8x8Fibonacci object instantiation
```

Behavior
-----

The Led8x8Fibonacci class manages the timing of the update and also resets itself after a maximum 64 bit fibonacci number is computed. The maximum fibonacci that can be represented by a 64 bit value is ...
```
7,540,113,804,746,346,429
```
