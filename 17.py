print("Mass in grams:")
mass = int(input())
print("Temperature in Celsius:")
dtemp = int(input())
q = 4.186 * mass * dtemp
print("The total energy in Joules: %f" %q)