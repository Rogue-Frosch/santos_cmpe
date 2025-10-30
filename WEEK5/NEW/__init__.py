strONE = "wuba"
strTWO = "luba"
strTHREE = "dubdub"
strFULL ="".join([strONE, strTWO, strTHREE])
print(strFULL)

newValue = strFULL.isnumeric
print(newValue)

newValue = strFULL[6:9]
print(newValue)
newValue = strFULL[6:9:2]
print(newValue)

print(strFULL.index("u"))
print(strFULL.index("u", 2, 9))
