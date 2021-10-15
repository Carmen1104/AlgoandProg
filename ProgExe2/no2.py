x = float(input("Enter length of edge1:"))
y = float(input("Enter length of edge2:"))
z = float(input("Enter length of edge3:"))

if x + y > z:
    if x + z > y:
        if z + y > x:
            perimeter = x+y+z
            print("The perimeter is ",perimeter)
else:
    print("Perimeter cannot be calculated. Your input is invalid!")

