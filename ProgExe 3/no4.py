import fractions

def calcNewHeight ():
    IWidth = float(input("Enter the current width: "))
    IHeight = float(input("Enter the current height: "))
    ratio = fractions.fromfloat(IWidth,IHeight)
    DWidth = float(input("Enter the desired width: "))
    Dheight = ratio * DWidth
    print("The corresponding height is ", Dheight)

calcNewHeight()