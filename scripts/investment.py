#!usr/bin/env python3

amount = float(input('Enter a amount: '))
inrate = float(input('Enter a Interest rate: '))
period = int(input('Enter a period: '))

value = 0
year = 1

while year < period : 
    value = amount + (inrate * amount)
    print('Year %d Rs. %2f' % (year, value))
    amount = value
    year = year + 1