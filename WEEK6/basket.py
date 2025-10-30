charA = ["Luffy", "Zoro", "Nami", "Ussop", "Sanji"]
charB = ["Naruto", "Sasuke", "Sakura", "Kakashi", "Sai"]
charC = ["Ichigo", "Rukia", "Uryu", "Renji", "Urahara"]

Character_list = [charA, charB, charC]
print(Character_list)
print(Character_list[1])
print(Character_list[2][1])

Character_list = charA + charB + charC
print(Character_list)

charA.extend(charB)
charA.extend(charC)
print(charA)