strFullName = "Prince Zhiljhon Geronimo Santos"

strModified = strFullName.capitalize()
print(strModified)

strModified = strFullName.count("o")
print(strModified)

strModified = strFullName.upper()
print(strModified)

strModified = strFullName.split(" ")
print(strModified)

strModified = strFullName.swapcase()
print(strModified)

strModified = strFullName.replace("Prince Zhiljhon","Zild")
print(strModified)

strModified = strFullName.replace(" ","...")
print(strModified)
print(" ")
print(" ")
print(" ")

strFirst = "Moyu"
strMid = "Gan"
strLast = "Tornado"
strFullName = "_".join([strFirst, strMid, strLast])
print("Good morning,", strFullName)

strFirst = "Terizla"
strMid = "Arlott"
strLast = "Cici"
strFullName = "_".join([strFirst, strMid, strLast])
print(strFullName)

newValue = strFullName.isnumeric()
print(newValue)

newValue = strFullName[3:6]
print(newValue)
newValue = strFullName[3:6:4]
print(newValue)
print(strFullName.index("r"))
print(strFullName.index("r",3,9))