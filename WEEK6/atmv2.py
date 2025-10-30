ATMMachineDataBase = [
    {
        "Name": {"LastName": "Baba", "FirstName": "Yaga"},
        "AccountNo": 9876482,
        "PIN": 967574,
        "ControlNo": 34254654,
        "Balance": .5
    },
    {
        "Name": {"LastName": "jan", "FirstName": "weak"},
        "AccountNo": 432424,
        "PIN": 1234,
        "ControlNo": 896,
        "Balance": 9999999
    },
    {
        "Name": {"LastName": "Wall-E", "FirstName": "Baloya"},
        "AccountNo": 453245646,
        "PIN": 3244,
        "ControlNo": 98417,
        "Balance": 6969696
    }
]

myName = input("Enter your first name: ")
PIN = int(input("Enter your PIN: "))

found = False

for account in ATMMachineDataBase:
    if account["Name"]["FirstName"].lower() == myName.lower() and account["PIN"] == PIN:
        print(f"Good Day, {myName}! Your balance is ₱{account['Balance']:.2f}.")
        found = True
        break

if not found:
    print("Invalid name or PIN. Please try again.")