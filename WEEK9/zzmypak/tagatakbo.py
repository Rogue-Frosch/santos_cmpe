
from WEEK9.Capacitor import Capacitance
from WEEK9.Inductor import Inductance
from WEEK9.Resistor import Resistance

selector = input("Please select Calculator")

while True:
    selector = input("Please select calculator: ")

    match selector.upper():
        case "CC_CV":
            print("Capacitance Calculator")

            charge = float(input("Please enter charge: "))
            voltage = float(input("Please enter voltage: "))

            Capacitance.get_capacitance_by_CV(charge, voltage)

        case "R_OHM":
            print("Resistance OHM'S LAW")

            current = float(input("Please enter current: "))
            voltage = float(input("Please enter voltage: "))

            Resistance.get_resistance_by_ohms_law(voltage, current)

        case "L_REAL":
            print("Inductive Resistance Calculator")

            frequency = float(input("Please enter frequency: "))
            inductance= float(input("Please enter reactor: "))

            Inductance.inductive_reactance(frequency, inductance)

        case _:
            print("NO MATCHING CASE, PLEASE SELECT AGAIN")
