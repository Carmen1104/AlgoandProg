#class definition
class ShopList:
    #Initializer method
    def __init__(self, name, amount):
        self.__name = name
        self.__amount = amount
        self.__standardPrice = self.__ShoppingListCC()
        self.__totalPrice = self.setCalcPriceCC()

    #Public Mutator method
    def setName(self, name):
        self.__name = name
    def setAmount(self, amount):
        self.__amount = amount
    def __ShoppingListCC(self):
        if self.__name == 'Dry Cured Iberian Ham':
            self.__standardPrice = 177.80
        elif self.__name == 'Wagyu Steaks':
            self.__standardPrice = 450.00
        elif self.__name == 'Matsutake Mushrooms':
            self.__standardPrice = 272.00
        elif self.__name == 'Kopi Luwak Coffee':
            self.__standardPrice = 306.50
        elif self.__name == 'Moose Cheese':
            self.__standardPrice = 487.20
        elif self.__name == 'White Truffles':
            self.__standardPrice = 3600.00
        elif self.__name == 'Blue Fin Tuna':
            self.__standardPrice = 3603.00
        elif self.__name == 'le Bonnotte Potatoes':
            self.__standardPrice = 270.81
        else:
            self.__standardPrice = 0.00

        return self.__standardPrice

    #Public Mutator method
    def setCalcPriceCC(self):
        self.__totalPrice = self.__amount * self.__standardPrice
        return self.__totalPrice

    #Accessor method
    def getName(self):
        return self.__name
    def getAmount(self):
        return self.__amount
    def getstandardPriceCC(self):
        return self.__standardPrice
    def getCalcPriceCC(self):
        return self.__totalPrice

    #__str__ method
    #def __str__(self):
    #   return "Item: {} , \nAmount ordered: {}, \nPrice per pound: {:.2f} , \nPrice of order: {:.2f}" .format(self.__name , 
    #        self.__amount , self.__standardPrice , self.__totalPrice)
