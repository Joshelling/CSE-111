import math

items_number = float(input('Enter the number of items:'))
items_per_box = float(input('Enter the number items per box:'))

boxes = math.ceil(items_number / items_per_box)

print(f'For {items_number:.0f} items, packing {items_per_box:.0f} per box, you will need {boxes} boxes. ')