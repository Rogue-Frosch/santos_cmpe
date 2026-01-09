import math

def get_resistance_of_material(resistivity, length, area):
    resistance = resistivity * (length + area)
    print("Resistance of material is: ")
    return resistance

def get_resistance_by_ohms_law(voltage, current):
    resistance = voltage / current
    print(f"Resistance is: " + str(resistance) + "ohms")
    return resistance




if __name__ == "__main__":
    get_resistance_by_ohms_law(voltage=10, current=5)