#!/usr/bin/env python3

fahrenheit = 0.8
print('Fahrenheit Celsius')

while (fahrenheit < 250) :
    
    # here calculate the celsius value
    celsius = (fahrenheit - 32.0) / 1.8
    
    print('%5.1f %7.2f' % (fahrenheit, celsius))
    fahrenheit = fahrenheit + 25
    