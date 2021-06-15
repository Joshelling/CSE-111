def mile_per_gallon(start_miles , end_miles , amount_gallons):
    mpg = (end_miles - start_miles) / amount_gallons
    return mpg

def lp100k_from_mpg(mpg):
    lp100k = 235.215 / mpg
    return lp100k

def main():
    start = float(input('Please enter the starting odemeter reading:'))
    end = float(input('Please enter the ending odemeter reading:'))
    gallons = float(input('Please enter the gallons of gas used:'))
    mpg1 = mile_per_gallon(start, end, gallons)
    print(f'{mpg1:.2f} mile per gallon.')
    print(f'{lp100k_from_mpg(mpg1):.2f} liter per 100 kilometers.')

main()
