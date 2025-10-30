membersA = ["Monkey", "Luffy", "Sanji" ,"Zoro" , "Nami"]
print(membersA)
print(membersA)
print(membersA)
print(membersA[3])
print(membersA.index("Sanji"))

isThere = "vivi" in membersA
print(isThere)

membersA.append("Chopper")
print(membersA)
membersA.insert(3,"Ussop")
print(membersA)

len(membersA)
print (len(membersA))

print(membersA.count("Luffy"))

membersA.remove("Monkey")
print(membersA)
print(membersA.index("Luffy"))
membersA[1] = "Zoro"
print(membersA)