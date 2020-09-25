print("Mass:")
m = int(input())
print("Temperature:")
dtemp = int(input())
q = 4.186 * m * dtemp
print("The total energy: %f" %q)
costincents = (8.9 * q) / 3600000
cost = costincents / 100
print("The total cost is %f dollars" %cost)
