# Lab 4
# Fourth lab, started with two items. Asks for input from user on amount they're purchasing of both items and calculates price, tax, and totalcost.
# Creates a string constant of the items
nameOfItem1 = 'Coffee'
nameOfItem2 = 'Muffin'

# Creates a int variable of the items purchased
numberOfItemsPurchased1 = 0
numberOfItemsPurchased2 = 0

# Creates a int constant for the prices
priceOfItem1 = 5.00
priceOfItem2 = 4.00
# two lines for seperation of variables and code


# asks user for input on amount purchased
numberOfItemsPurchased1 = int(input("How many coffees are you purchasing? "))
numberOfItemsPurchased2 = int(input('How many muffins are you purchasing? '))

# calculates both totals of items, and then adds the two totals for totalItemCost
itemTotal1 = numberOfItemsPurchased1 * priceOfItem1 
itemTotal2 = numberOfItemsPurchased2 * priceOfItem2
totalItemCost = itemTotal1 + itemTotal2

# sets a int constant for the tax percent, creates tax cost and then adds taxCost to totalItemCost for totalCost
tax = 0.06
taxCost = totalItemCost * tax
totalCost = taxCost + totalItemCost

# prints first receipt
print('*************************************')
print('My Coffee and Muffin Shop Receipt')
print('Number of coffees bought?')
print(numberOfItemsPurchased1)

print('Number of muffins bought?')
print(numberOfItemsPurchased2)
print('************************************* \n')

# prints receipt and uses the constants and variables to print the number of items purchased, name of items
# price of items, and item total costs, then tax cost, and total cost.
print('*************************************')
print('My Coffee and Muffin Shop Receipt')
print(numberOfItemsPurchased1, nameOfItem1, 'at $', priceOfItem1, 'each: $ ', itemTotal1 )
print(numberOfItemsPurchased2, nameOfItem2, 'at $', priceOfItem2, 'each: $ ', itemTotal2 )
print('6% tax: $', taxCost)
print('---------')
print('Total: $', totalCost)
print('*************************************')