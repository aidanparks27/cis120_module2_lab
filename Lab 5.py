# Lab 5
# Aidan Parks 
# 10/24/2024
# Tracking total number of bottles collected for seven days through count-controlled loops

def main():
    totalBottles = 0
    totalPayout = 0.0
    keepGoing = 'y'
    PRICE_PER_BOTTLE = 0.10
    

    while keepGoing == 'y':
        totalBottles = getBottles()
        totalPayout = totalBottles* PRICE_PER_BOTTLE
        printTotalPayout(totalBottles, totalPayout)
        keepGoing = input('Keep Going? ( y or n)')
        if keepGoing == 'n':
            print('>>>')

def getBottles():
        NBR_OF_DAYS = 7
        totalBottles = 0
        todayBottles = 0
        counter = 1

        while counter <= NBR_OF_DAYS:
            todayBottles = \
            int(input(f'Bottles for day{counter}'))
            totalBottles += todayBottles
            counter += 1
        return totalBottles
    
def printTotalPayout(x,y):
     print(f'Amount of Bottles is :{x}')
     print(f'Total cost:{y:.2f}')

main()