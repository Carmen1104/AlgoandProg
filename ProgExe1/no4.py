import math

side = eval(input("Enter the side length of the hexagon:"))

area = (math.sqrt(27)/2) * pow(side,2)

print("The area of the hexagon with side length", side, "is", "{:,.3f}".format(area))