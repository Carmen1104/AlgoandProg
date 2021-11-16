import os

#Input original text file
filename = input("Enter file name:")
file = open(os.getcwd()+"\\"+filename,"r") 
outputFile = open("newtext.txt","w")

count=0
for line in file:
    count +=1
    outputFile.write("{:2d}: {}".format(count,line))
    
outputFile.close()
file.close()
