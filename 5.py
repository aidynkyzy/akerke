one_liter_less_container = int(input("Enter the number of one liter less containers you recycled: "))

one_liter_more_container = int(input("Enter the number of one liter more containers you recycled: "))

refund = (one_liter_less_container * 0.10) + (one_liter_more_container * 0.25)

print("The total refund for returning the containers is $" + "{0:.2f}".format(float(refund)))