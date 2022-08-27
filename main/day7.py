#day 7, Sales data organization

#make a list of pizza & prices in 2d list
pizza_and_prices = [[2.00, "pepperoni"], [6.00, "pineapple"], [1.00, "cheese"], [3.00, "sausage"], [2.00, "olives"], [7.00, "anchovies"], [2.00, "mushrooms"]]

print(pizza_and_prices)

#sort pizza prices in increasing manner
pizza_and_prices.sort()

#store cheapest pizza
cheapest_pizza = pizza_and_prices[0]

#store most expensive pizza
priciest_pizza = pizza_and_prices[-1]

#ran out of a slice so remove it
pizza_and_prices.pop()

#customer wants 3 cheapest slices
three_cheapest = pizza_and_prices[:3]

print()
print()

print(three_cheapest)
