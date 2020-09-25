a=int(input('Enter an amount between 0-99:'))
print(a//25, "quarters")
a = a%25
print(a//10, "dimes")
a = a%10
print(a//5, "nickles")
a = a%5
print(a//1, "pennies")
