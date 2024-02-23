import random

file = open("testfile.txt", "r")
readData = file.read().splitlines()
print(readData)

if readData:
    randomWord = random.choice(readData)
    print(randomWord)
else:
    print("empty file")