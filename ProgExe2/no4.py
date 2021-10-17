
qty = int(input("Enter the number of packages purchased: "))
price = 99

if (qty < 10):
    disc = 0
    print("Discount amount at 0%:","${:.2f}".format(disc))
elif (qty < 20):
    disc = ((price * qty) / 100) * 10
    print("Discount amount at 10%:","${:.2f}".format(disc))
elif (qty < 50):
    disc = ((price * qty) / 100) * 20
    print("Discount amount at 20%:","${:.2f}".format(disc))
elif (qty < 99):
    disc = ((price * qty) / 100) * 30
    print("Discount amount at 30%:","${:.2f}".format(disc))
else:
    disc = ((price * qty) / 100) * 40
    print("Discount amount at 40%:","${:.2f}".format(disc))

totam = qty*price - disc
print("Total amount:","${:.2f}".format(totam))


