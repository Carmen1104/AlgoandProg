
x = True

temp = int(input("Enter the temperature in Fahrenheit: "))
while not (-58<temp<41):
    print("Temperature must be between -58F to 41F")
    temp = int(input("Please re-enter the temperature in Fahrenheit: "))
else:
    x = False

ws = int(input("Enter the wind speed miles per hour: "))
while not(ws >= 2):
    print("Speed must be greater than or equal to 2")
    ws = int(input("Please re-enter the wind speed miles per hour: "))
else:
    x = False

twc = 35.74 + (0.6215*temp) - 35.75*pow(ws,0.16) + 0.4275*temp*pow(ws,0.16)

print("The wind chill index is ", end="")
print("{:,.3f}".format(twc))
    
    

