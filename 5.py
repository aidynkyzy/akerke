liter_less= int(input("Enter the number of one liter less containers you recycled: "))

liter_more = int(input("Enter the number of one liter more containers you recycled: "))

refund = (liter_less * 0.10) + (liter_more * 0.25)

print("The total refund for returning the containers is $" + "{0:.2f}".format(float(refund)))
