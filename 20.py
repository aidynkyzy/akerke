print("The pressure in Pascals:")
p = float(input())
print("The volume in liters:" )
v = float(input())
print("The temperature in degrees Kelvin:")
t = float(input())
n = (p * v)/(8.314 * t)
print("The amount of substance in moles: %f" %n)