
def convertToDays():
    global H
    global M
    global S
    H = float(input('Enter number of hours: '))
    M = float(input('Enter number of minutes: '))
    S = float(input('Enter number of seconds: '))

def getDays():
    days = ((60*60*H)+(60*M)+S)/(86400)
    print(round(days,4))

convertToDays()
getDays() 
