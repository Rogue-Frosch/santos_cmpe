'''

print("before loop")

for i in range(10):
    if i % 2 == 0:
        print("even number : " + str(i))
        continue
    elif i > 7:
        print("i is greater than 7 : ")
        break

    print("i value now is  : " + str(i))

print("after loop")

'''

'''

import time

isConnected = "No"

for retry in range(5):
    time.sleep(2)
    isConnected = input("is connected?")
    if isConnected == "yes":
        print("kunekted")
        break
    else:
        print("dili kunekted")

print("sandale....")

'''
'''

#nested

for i in range(10):
    print(str(i) + "ayoko say0")
    for x in range(10):
        print(x)

'''

charlist = [
'a', "b", "c", "d", "e", "f", "g", "h", "i", "j", "k","l", "m",
"n", "o", "p", "q", "r", "s", "t", "u", "v","w", "x", "y", "z",
"A", "B", "C", "D", "E", "F", "G","H", "I", "J", "K", "L", "M",
"N", "O", "P", "Q", "R","S", "T", "U", "V", "W", "X", "Y", "Z",
"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

#simple encryption
myinput = "Hello 1234"
output = ' ' #"Khoor4567"
key = 3
indexCounter = 0

for letter in myinput:
    indexCounter = charlist.index(letter)
    print(indexCounter)
    output = output + charlist[indexCounter + key]

print(output)