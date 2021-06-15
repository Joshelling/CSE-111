import random

def main():
    randnums = [16.2, 75.1, 52.3]
    print(f'Randnums {randnums}')
    append_random_numbers(randnums)
    print(f'Randnums {randnums}')

    append_random_numbers(randnums, 3)
    print(f'Randnums {randnums}')




def append_random_numbers(numbers_list, quantity=1):
    for _ in range(quantity):
        quan = random.uniform(0, 100)
        quan1 = round(quan, 1)
        numbers_list.append(quan1)
       


main()
