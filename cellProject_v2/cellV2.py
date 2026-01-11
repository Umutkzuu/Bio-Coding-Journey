from organellesV2 import *

class Cell:
    def __init__(self, dna_code):
        self.atp_storage = 20
        self.waste_amount = 5
        self.toxin_level = 0
        
        self.raw_protein = 0
        self.processed_protein = 0
        self.membrane_material = 0 
        
        self.lipid_stock = 0       
        self.structural_integrity = 100
        self.is_alive = True
        
        self.organelles = []
        
        self.add_organelle(Nucleus(dna_code))
        self.add_organelle(Mitochondria())
        self.add_organelle(Ribosome())
        self.add_organelle(RoughER())
        self.add_organelle(SmoothER())
        self.add_organelle(GolgiApparatus())
        self.add_organelle(Lysosome())
        self.add_organelle(Peroxisome())
        self.add_organelle(Cytoskeleton())
        self.add_organelle(Centrosome())

    def add_organelle(self, organelle):
        self.organelles.append(organelle)

    def life_cycle(self):
        if not self.is_alive:
            print("[DEAD] Cell function ceased.")
            return

        print(f"\n=== CELL STATUS ===")
        print(f"ATP: {self.atp_storage} | Toxins: {self.toxin_level} | Health: {self.structural_integrity}%")
        print(f"Stocks -> Raw Prot: {self.raw_protein} | Processed: {self.processed_protein} | Membrane: {self.membrane_material}")
        print("-------------------")
        
        for organelle in self.organelles:
            organelle.operate(self)
            
        self.check_vital_signs()

    def check_vital_signs(self):
        if self.atp_storage <= 0:
            self.is_alive = False
            print("\n!!! DEATH CAUSE: Starvation (No ATP) !!!")
        elif self.toxin_level > 20:
            self.is_alive = False
            print("\n!!! DEATH CAUSE: Toxicity !!!")
        elif self.structural_integrity <= 0:
            self.is_alive = False
            print("\n!!! DEATH CAUSE: Structural Collapse !!!")