import os
filename = input("Enter file name:")
myfile = open(os.getcwd()+"\\"+filename,"r")
wordcount_sum = 0
wordlength_sum = 0
for line in myfile:
    words = line.split()
    # sum up the word counts
    wordcount_sum += len(words)
    for word in words:
        # sum up the word lengths
        wordlength_sum += len(word)
        print(wordlength_sum)