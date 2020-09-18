cost_of_feed = int(input("Enter the cost of food: "))

tax = 1.05

cost_of_feed_tax = tax * cost_of_feed

tip = 1.15

cost_of_feed_tip = tip * cost_of_feed_tax


print("With tax: {}".format(cost_of_feed_tax))
print("With tip: {}".format(cost_of_feed_tip))
                   