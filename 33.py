loaves = int(input("Amount of loaves: "))

price = loaves*3.49
discount = price*0.6
total_price = price - discount

print("Price of the bread", price)
print("Value of discount:", discount)
print("Total price:", total_price)