import time
import os
from operator import truediv

amount = 0
balance = 67000
pin_number = "145610"

def welcome_message():
    time.sleep(1)
    print("WELCOME TO THE NYA BANK SYSTEM")
    time.sleep(1)
    print("-------------------------")
    time.sleep(1)
    print("PLEASE ENTER YOUR CARD")

def card_reader(isCardInserted):
    if isCardInserted == "YES":
        print("Card is inserted")
        return True
    else:
        return False

def input_and_validate_pin_number(inputPinNumber):
    for i in range(4):
        if i == 3:
            print("Card is blocked, punta ka bank boi")
            return False
        inputPinNumber = input("Please Input your Pin Number")
        if inputPinNumber == pin_number:
            return True
        else:
            print("UR BERI BERI RONG")

def transaction_selection():
    transaction = input("Please Input your Transaction Type")
    return transaction


def transaction_validation(amount, balance):
    if balance >= amount:
        re


while True:
    welcome_message()
    isCardInserted = input("Is card inserted?")
    if not card_reader(isCardInserted):
        continue
    print("Next Steps")
    inputPinNumber = input("Please enter pin number")
    input_and_validate_pin_number(inputPinNumber)