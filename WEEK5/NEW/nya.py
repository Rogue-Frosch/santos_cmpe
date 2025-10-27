strInput = "9438174d921408124i0325835029t34o9284 948k100a 93n18237a233l199a231n3218g93"

newString = " "
for char in strInput:
    if not char.isnumeric():
        newString = newString + char

print(newString)