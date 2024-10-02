# Lab 4
# Fourth lab, started with two items. Asks for input from user on amount they're purchasing of both items and calculates price, tax, and totalcost.
# Creates a string constant of the items
nameOfItem1 = 'Coffee'
nameOfItem2 = 'Muffin'
nameOfItem3 = 'Pizza'
nameOfItem4 = 'Donut'


# Creates a int variable of the items purchased
numberOfItemsPurchased1 = 0
numberOfItemsPurchased2 = 0
numberOfItemsPurchased3 = 0
numberOfItemsPurchased4 = 0

# Creates a int constant for the prices
priceOfItem1 = 5.00
priceOfItem2 = 4.00
priceOfItem3 = 3.00
priceOfItem4 = 2.00
# two lines for seperation of variables and code


# asks user for input on amount purchased
numberOfItemsPurchased1 = int(input("How many coffees are you purchasing? "))
numberOfItemsPurchased2 = int(input('How many muffins are you purchasing? '))
numberOfItemsPurchased3 = int(input('How many pizzas are you purchasing? '))
numberOfItemsPurchased4 = int(input('How many donuts are you purchasing? '))


# calculates both totals of items, and then adds the two totals for totalItemCost
itemTotal1 = numberOfItemsPurchased1 * priceOfItem1 
itemTotal2 = numberOfItemsPurchased2 * priceOfItem2
itemTotal3 = numberOfItemsPurchased3 * priceOfItem3
itemTotal4 = numberOfItemsPurchased4 * priceOfItem4

totalItemCost = itemTotal1 + itemTotal2 + itemTotal3 + itemTotal4

# sets a int constant for the tax percent, creates tax cost and then adds taxCost to totalItemCost for totalCost
tax = 0.06
taxCost = totalItemCost * tax
totalCost = taxCost + totalItemCost

# prints first receipt
print('*************************************')
print('My Amazing Shop Receipt')
print('Number of coffees bought?')
print(numberOfItemsPurchased1)

print('Number of muffins bought?')
print(numberOfItemsPurchased2)

print('Number of pizzas bought?')
print(numberOfItemsPurchased3)

print('Number of donuts bought?')
print(numberOfItemsPurchased4)
print('************************************* \n')

# prints receipt and uses the constants and variables to print the number of items purchased, name of items
# price of items, and item total costs, then tax cost, and total cost.
print('*************************************')
print('My Amazing Shop Receipt')

print(numberOfItemsPurchased1, nameOfItem1, 'at $', priceOfItem1, 'each: $ ', itemTotal1 )
print(numberOfItemsPurchased2, nameOfItem2, 'at $', priceOfItem2, 'each: $ ', itemTotal2 )
print(numberOfItemsPurchased3, nameOfItem3, 'at $', priceOfItem3, 'each: $ ', itemTotal3 )
print(numberOfItemsPurchased4, nameOfItem4, 'at $', priceOfItem4, 'each: $ ', itemTotal4 )

print('6% tax: $', taxCost)
print('---------')
print('Total: $', totalCost)
print('*************************************')

print('Thank you for shopping at My Amazing Shop! Come again!')
