length = float(input('Enter the field length in feet: '))
width = float(input('Enter the field length in feet: '))
feet_in_an_acre = 43560
area = (length * width) / feet_in_an_acre
print('Area of the field {} acre'.format(area))