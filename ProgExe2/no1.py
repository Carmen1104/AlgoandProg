import math

m = int(input("Enter the mass of the cart (in kg):"))
f = int(input("Enter the force to push the cart (in N):"))
g = 9.8

angle = f / m / g
sine =math.asin(angle)
sine =math.degrees(sine)

print("The angle of the ramp is ", end ="")
print ("{:,.1f}".format(sine), "degrees")