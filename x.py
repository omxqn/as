
def displayMenu():
    choices = { 1:"Add order",
                2:"Display order",
                3:"Display all orders",
                4:"Display orders per customer",
                5:"Display orders per country",
                6:"Display orders statistics",
                7:"Remove order",
                8:"Exit program"
              }
    print('''****************************************
		 Al-Yaqeen Logistics
****************************************''')
    for i in choices:
        print(f"{i}) ",choices[i])
def addOrder():
    pass
def displayOrder():
    pass
def displayAllOrders():
    pass
def displayCustomerOrders():
    pass
def displayCountryOrders ():
    pass
def displayStatistics():
    pass
def removeOrder():
    pass
def main():
    displayMenu()

main()