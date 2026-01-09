import math


def get_inductor_value_of_material(relativeP, permiability, turns, area, length):
    inductance = (relativeP * permiability * turns * turns * area) / length
    print(f"Inductance is: " + str(inductance) + "ohms")

def get_inductive_reactance(Voltage, Current):
    reactance = Voltage / Current
    print("The inductive reactance is: ", reactance)
    return reactance



if __name__ == "__main__":
    get_inductive_reactance( frequency=1000, inductance=0.000067 )