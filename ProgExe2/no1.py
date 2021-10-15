import math

mass = int(input("Enter the mass of the cart (in kg):"))
force = int(input("Enter the force to push the cart (in N):"))

angle = force / (mass * 9.8)
sine =math.asin(angle)

print("The angle of the ramp is ", end ="")
print ("{:,.1f}".format((math.degrees(sine))))