import math 
def main():
    
    picnic_radius = 6.83
    picnic_height = 10.16
    picnic_surface_area = compute_cone_surface_area(picnic_radius, picnic_height)
    picnic_volume = compute_cone_volume(picnic_radius, picnic_height)
    print(f'The storage effiency of the #1 picnic is {storage_effiency(picnic_volume, picnic_surface_area):.2f}.')
    tall_radius = 7.78
    tall_height = 11.91
    tall_surface_area = compute_cone_surface_area(tall_radius, tall_height)
    tall_volume = compute_cone_volume(tall_radius, tall_height)
    print(f'\nThe storage effiency of #1 Tall is {storage_effiency(tall_volume, tall_surface_area):.2f}')
    two_radius = 8.73
    two_height = 11.59
    two_surface_area = compute_cone_surface_area(two_radius, two_height)
    two_volume = compute_cone_volume(two_radius, two_height)
    print(f'\nThe storage effiency of #2 is {storage_effiency(two_volume, two_surface_area):.2f}')
    two_five_radius = 10.32
    two_five_height = 11.91
    two_five_surface_area = compute_cone_surface_area(two_five_radius, two_five_height)
    two_five_volume = compute_cone_volume(two_five_radius, two_five_height)
    print(f'\nThe storage effiency of #2.5 is {storage_effiency(two_five_volume, two_five_surface_area):.2f}')
    three_radius = 10.79
    three_height = 17.78
    three_surface_area = compute_cone_surface_area(three_radius, three_height)
    three_volume = compute_cone_volume(three_radius, three_height)
    print(f'\nThe storage effiency of #3 Cylinder is {storage_effiency(three_volume, three_surface_area):.2f}')
    five_radius = 13.02
    five_height = 14.29
    five_surface_area = compute_cone_surface_area(five_radius, five_height)
    five_volume = compute_cone_volume(five_radius, five_height)
    print(f'\nThe storage effiency of #5 is {storage_effiency(five_volume, five_surface_area):.2f}')
    six_radius = 5.40
    six_height = 8.89
    six_surface_area = compute_cone_surface_area(six_radius, six_height)
    six_volume = compute_cone_volume(six_radius, six_height)
    print(f'\nThe storage effiency of #6Z is {storage_effiency(six_volume, six_surface_area):.2f}')
    eigth_radius = 6.83
    eight_heigth = 7.62
    eight_surface_area = compute_cone_surface_area(eigth_radius, eight_heigth)
    eight_volume = compute_cone_volume(eigth_radius, eight_heigth)
    print(f'\nThe storage effiency of #8Z short is {storage_effiency(eight_volume, eight_surface_area):.2f}')
    ten_radius = 15.72
    ten_height = 17.78 
    ten_surface_area = compute_cone_surface_area(ten_radius, ten_height)
    ten_volume = compute_cone_volume(ten_radius, ten_height)
    print(f'\nThe storage effiency of #10 is {storage_effiency(ten_volume, ten_surface_area):.2f}')
    two_eleven_radius = 6.83
    two_eleven_height = 12.38
    two_eleven_surface_area = compute_cone_surface_area(two_eleven_radius, two_eleven_height)
    two_eleven_volume = compute_cone_volume(two_eleven_radius, two_eleven_height)
    print(f'\nThe storage effiency of #211 is {storage_effiency(two_eleven_volume, two_eleven_surface_area):.2f}')
    three_hundred_radius = 7.62 
    three_hundred_heigth = 11.27
    three_hundred_surface_area = compute_cone_surface_area(three_hundred_radius, three_hundred_heigth)
    three_hundred_volume = compute_cone_volume(three_hundred_radius, three_hundred_heigth)
    print(f'\nThe storage effiency of #300 is {storage_effiency(three_hundred_volume, three_hundred_surface_area):.2f}')
    three_o_three_radius = 8.10
    three_o_three_height = 11.11
    three_o_three_surface_area = compute_cone_surface_area(three_o_three_radius, three_o_three_height)
    three_o_three_volume = compute_cone_volume(three_o_three_radius, three_o_three_height)
    print(f'\nThe storage effiency of #303 is {storage_effiency(three_o_three_volume, three_o_three_surface_area):.2f}')
    





def compute_cone_volume(radius, height):
  
    volume = math.pi * (radius**2) * height
    return volume







def compute_cone_surface_area(radius, height):
    
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area



def storage_effiency(volume, surface_area):
    storage = volume / surface_area
    return storage


main()