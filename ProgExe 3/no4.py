def calcNewHeight ():
    IWidth = float(input("Enter the current width: "))
    IHeight = float(input("Enter the current height: "))
    DWidth = float(input("Enter the desired width: "))
    DHeight = ((IHeight * DWidth) / IWidth)
    print("The corresponding height is ", DHeight)

calcNewHeight()
