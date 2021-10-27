
def convertTemp ():
    global Tf
    Tf = float(input("Enter a temperature in Fahrenheit: "))

    def convertToCelcius():
        global Tc
        Tc = (5/9)*(Tf - 32)
    convertToCelcius()

    def convertToKelvin():
        global Tk
        Tk = Tc + 273.15
    convertToKelvin()
    
    print("The temperature in Fahrenheit is :", Tf)
    print("The temperature in Celcius is :", Tc)
    print("The temperature in Kelvin is :", Tk)

convertTemp()


    