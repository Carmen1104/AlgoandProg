
v = eval(input("Enter the plane's take speed in m/s: "))
a = eval(input("Enter the plane's acceleration in m/s**2: "))

length = (v**2) / (a*2)
print("The minimun runway length for this airplane is", "{0:.4f}".format(length), "meters.")