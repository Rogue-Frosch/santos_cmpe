Kulayko = input("Please input your color: ")

if Kulayko == "black":
    print("ayooo wassup")
elif Kulayko == "yellow":
    print("Irishaimasen")
elif Kulayko == "brown":
    print("kamusta")
elif Kulayko == "white":
    print("nice to meet you")
else:
    print("nuka alien")


heightincm = int(input("Enter height in cm: "))

if heightincm >= 200:
    print("waw tangkad")
elif heightincm >= 180:
    print("saks lang")
elif heightincm >= 160:
    print("hahahahha!!!")
else:
    print("nuka unano")
print("next po")


citizenship = "Filipino"
Age = 18
Registered = False

if citizenship == "Filipino" and Age >= 18:
    if Registered:
        print("Boto na")
    else:
        print("Bawal ka boi, galawgalaw kasi")
elif citizenship ==  "Filipino" and Age < 18:
    print("Bawal pa, kalmahan mo")
else:
    print("Ekis ka talaga boi")