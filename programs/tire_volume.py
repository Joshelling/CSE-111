import math
from datetime import datetime

current_day = datetime.now()

width = float(input('Please enter the width of the tire in MM (Ex 205):'))
ar = float(input('Please enter the aspect ratio of the tire (Ex 60):'))
diameter = float(input('Please enter the diameter of the tire (Ex 15):'))
rotate = float(input('How many miles have you driven since your tires were rotated:'))
user_input = input('Would you like to buy new tires for your vehicle. (yes/no)')

if user_input == 'yes':
    name = input('Please enter your full name:')
    phone_number = input('Please enter your phone number:')


if rotate > 5000:
    print('It is time to have your tires rotated.')
else:
    # print('Your tires do not need to be rotated.')
    print(f'{5000 - rotate} is the number of miles until your tires will need to be rotated.')


volume = math.pi * width**2 * ar 
volume2 = volume * (width * ar + 2540 * diameter)
volume3 = volume2 / 10000000
print(f'The approxiamte volume is {volume3:.1f} cubic cm.')

with open ('volumes.txt', 'at') as volume_collector:
    print(f'The date is: {current_day}, The width is: {width}, The Aspect Ratio is: {ar}, The diamter is: {diameter}', file=volume_collector)
    if user_input.lower() == 'yes':
        print(f'{name}, {phone_number}', file=volume_collector)

