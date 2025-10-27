unitA = {"Barbarian", "Archer", "Archer", "Giant", "Baloon"}
unitB = {"Archer", "Baloon", "Witch", "Valkyrie", "Golem"}
print(unitA)
print(unitB)

unitA.add("Wizard")
print(unitA)

unitUnion = unitA.union(unitB)
print(unitUnion)
unitIntersection = unitA.intersection(unitB)
print(unitIntersection)
unitDifference = unitA.difference(unitB)
print(unitDifference)
unitDifference = unitB.difference(unitA)
print(unitDifference)

unitA = {"Barbarian", "Archer", "Archer", "Giant", "Baloon"}
unitB = {"Archer", "Baloon", "Witch", "Valkyrie", "Golem"}
Unitlayoutlistofset = [unitA, unitB]
print(Unitlayoutlistofset)