import math

def get_capacitance_by_material(permeability, area, distance):
    dielectricCon = 8.854 * 10e-12
    Capacitance = (permeability * dielectricCon * area) / distance
    print(f"Capacitance of Material is:{Capacitance}")
    return Capacitance

def get_capacitance_by_CV(Charge, Voltage):
    Capacitance = Charge / Voltage
    print(f"Capacitance by CV:{Capacitance}")
    return Capacitance

def get_capacitance_current(capacitance, dvoverdt):
    ic = capacitance * dvoverdt
    print(f"Capacitance of Current is:{ic}")
    return ic

def get_capacitive_reaction(frequency, capacitance):
    reactance = 1 / (2 * math.pi * frequency * capacitance)
    print(f"Capacitance of Reaction is:{reactance}")
    return reactance


if __name__ == "__main__":
    get_capacitance_by_CV( Charge= 1000, Voltage= 1000)