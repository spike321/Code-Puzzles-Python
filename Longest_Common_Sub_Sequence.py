import sys

first_word = input()
second_word = input()
myList = [[]]

for x in range (0, len(first_word)):
    for y in range (0, len(second_word)):
        myList[x][y] = 0

print(myList)