
sub = float(input("Enter the subtotal:"))
tip = float(input("Enter tip amount (as a %) :"))

tip2 = sub * (tip/100)
total = sub + tip2

print("Subtotal","${:,.2f}".format(sub))
print("Tip","${:,.2f}".format(tip2))
print("Total","${:,.2f}".format(total))
