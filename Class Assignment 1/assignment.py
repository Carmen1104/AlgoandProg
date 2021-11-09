import os
os.getcwd()

def countWords(word):
    myDict = {}
    Split = word.split()
    for each in Split:
        myDict[each] = myDict.get(each,0)+1 
    return myDict

#Input original text file
filename = input("Enter file name:")
file = open(os.getcwd()+"\\"+filename,"r") 
text = file.read()
text1 = text.lower()
file.close()

#Turn all text to lower case
file2 = open("text2.txt", "w")
print(text1, file= open("text2.txt", "w"))
file.close()

#Counts hapaxes
file3 = open("text2.txt", "r")
word = file3.read()

myWordCount = countWords(word)

for key in myWordCount:
    if myWordCount[key] == 1:
        print(myWordCount[key],key)