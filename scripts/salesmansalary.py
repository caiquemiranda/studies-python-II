#!/usr/bin/env python3

basic_salary = 1.500
bonus_rate = 200
commision_rate = 0.2

numberofcamera = int(input('Enter the number of input sold: '))
price = float(input('Enter teh total prices: '))
bonus = (bonus_rate * numberofcamera)
commision = (commision_rate * numberofcamera * price)

print("Bonus        = %6.2f" % bonus)
print("Comission    = %6.2f" % commision)
print('Gross salary = %6.2f' % (basic_salary + bonus + commision))