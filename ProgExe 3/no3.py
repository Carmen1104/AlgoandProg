avogrado = 6.022 * pow(10,23)

def numAtoms (amt = 10 , weight = 196.97):
    atoms = (amt/weight) * avogrado
    print(atoms)
    return atoms

numAtoms()
