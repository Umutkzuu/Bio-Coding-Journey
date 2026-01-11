class Organelle: 

    def __init__(self, name):
        self.name = name

    def operate(self, cell):
        pass

    def __str__(self):
        return f"[{self.name}]"
    
class Nucleus(Organelle):

    def __init__(self, dna_code):
        super().__init__("Nucleus")
        self.dna_code = dna_code

    def operate(self, cell):
        if cell.atp_storage > 50 and cell.lipid_stock > 10:
            print(f"  -> {self} DNA replicated. Ready for Mitosis.")
        else:
            print(f"  -> {self} Managing instructions. DNA: {self.dna_code}")

class Mitochondria(Organelle):

    def __init__(self):
        super().__init__("Mitochondria")

    def operate(self, cell):

        prod = 15
        toxin = 1 
        cell.atp_storage += prod
        cell.toxin_level += toxin
        print(f"  -> {self} Aerobic respiration. +{prod} ATP, +{toxin} Toxin.")

class Ribosome(Organelle):
    def __init__(self):
        super().__init__("Ribosome")

    def operate(self, cell):
        cost = 5
        if cell.atp_storage >= cost:
            cell.atp_storage -= cost
            cell.raw_protein += 1 
            print(f"  -> {self} Synthesized RAW Protein. -{cost} ATP.")
        else:
            print(f"  -> {self} Low Energy. Idling.")


class RoughER(Organelle):
    def __init__(self):
        super().__init__("Rough Endoplasmic Reticulum")

    def operate(self, cell):
        if cell.raw_protein > 0:
            cell.raw_protein -= 1
            cell.processed_protein += 1
            print(f"  -> {self} Folded and processed a protein.")
        else:
            print(f"  -> {self} Waiting for raw proteins from Ribosome.")

class GolgiApparatus(Organelle):
    def __init__(self):
        super().__init__("Golgi Apparatus")

    def operate(self, cell):
        if cell.processed_protein > 0:
            cell.processed_protein -= 1
            cell.membrane_material += 1
            print(f"  -> {self} Packaged protein into vesicle. +1 Membrane Material.")
        else:
            print(f"  -> {self} Waiting for processed proteins from ER.")

class SmoothER(Organelle):
    def __init__(self):
        super().__init__("Smooth Endoplasmic Reticulum")

    def operate(self, cell):
        cost = 8
        if cell.atp_storage >= cost:
            cell.atp_storage -= cost
            cell.lipid_stock += 1
            print(f"  -> {self} Lipid synthesized. -{cost} ATP.")

class Lysosome(Organelle):
    def __init__(self):
        super().__init__("Lysosome")
    
    def operate(self, cell):
        if cell.waste_amount > 0:
            cell.waste_amount -= 2
            print(f"  -> {self} Digested cellular waste.")

class Peroxisome(Organelle):
    def __init__(self):
        super().__init__("Peroxisome")

    def operate(self, cell):
        if cell.toxin_level > 0:
            cell.toxin_level -= 2
            print(f"  -> {self} Neutralized toxins.")
        else:
            print(f"  -> {self} No toxins detected.")

class Cytoskeleton(Organelle):
    def __init__(self):
        super().__init__("Cytoskeleton")

    def operate(self, cell):
        maintenance_cost = 2
        if cell.atp_storage >= maintenance_cost:
            cell.atp_storage -= maintenance_cost
            cell.structural_integrity = 100
            print(f"  -> {self} Maintained cell shape.")
        else:
            cell.structural_integrity -= 20
            print(f"  -> {self} WARNING: Structure collapsing! Low Energy.")

class Centrosome(Organelle):
    def __init__(self):
        super().__init__("Centrosome")

    def operate(self, cell):
        if cell.membrane_material > 5:
            print(f"  -> {self} Spindle fibers forming. Ready for division.")
