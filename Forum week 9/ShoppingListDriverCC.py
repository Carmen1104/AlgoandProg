#import class module
from FancyShoppingListCC import ShopList

#Create list function
def createListCC():
    
    item = int(input("How many items do you want to buy? ")) #Asks for user to input amount of items
    li = []
    while not item >= 1:
        print("Number of items must be atleast 1.")
        item = int(input("How many items do you want to buy? "))       

    for i in range(item):
        print("Item #{}".format(i+1),"-")
        name = input("Enter food: ")

        amount = eval(input("Enter amount of pounds: "))
        while not amount >= 0:
            print("Amount of pounds must be greater than 0.")
            amount = eval(input("Enter amount of pounds: "))       
        print()
        li.append(ShopList(name, amount))
    
    return li

#Display List function
def displayListCC(list):
    print("Here's a summary of the items purchased:")
    print("----------------------------------------")
    for ShopList in list:
        print("Item: {}".format(ShopList.getName()))
        print("Amount ordered: {:.1f}".format(ShopList.getAmount()), "pounds")
        print("Price per pound: ${:.2f}".format(ShopList.getstandardPriceCC()))
        print("Price of order: ${:.2f}".format(ShopList.getCalcPriceCC()))
        print()

#Function to count the total cost
def totalCostCC(list):
    total = 0
    for i in list:
        total = i.getCalcPriceCC() + total
        print("Total cost: ${:.2f}".format(total))

#Main Function calls all the other function
def main():
    list = createListCC()
    displayListCC(list)
    totalCostCC(list)

#Test (Runs Code)
main()
