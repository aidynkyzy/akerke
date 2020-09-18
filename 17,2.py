print("Mass in grams:")
mass = int(input())
print("Temperature in Celsius:")
dtemp = int(input())
q = 4.186 * mass * dtemp
print("The total energy in Joules: %f" %q)
costincents = (8.9 * q) / 3600000
cost = costincents / 100
print("The total cost is %f dollars" %cost)