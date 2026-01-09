fruitlist = ["apple", "banana", "cherry", "orange", "strawberry"]

for fruit in fruitlist:
    print("fruit list include : " + str(fruit))

print("after loop")

mystring = ("hindi ko naman yata ikamamatay, kung hindi ko mahawakan ang iyong kamay "
            "handa kong mabuhay sa aking kalokohan kung wala ka saking buhay walang kalungkutan")
for char in mystring:
    print(char.upper())

originalValue = "ekoc omsim"

print("originalValue" + originalValue)
newValue = ""

for x in originalValue:
    newValue = x + newValue

print("newValue : " + newValue)

print(originalValue[::-1])