from organelles import Nucleus, Mithochondria, Ribosome, Lysosome

class Cell:

    def __init__(self, dna_code):
        self.atp_storage = 10
        self.protein_stock = 0
        self.waste_amount = 5
        self.is_alive = True


        self.organelles = []        

        print(f"Creating a new cell with DNA: {dna_code}")
        self.add_organelle(Nucleus(dna_code))
        self.add_organelle(Mithochondria())
        self.add_organelle(Ribosome())
        self.add_organelle(Lysosome())
        print("------------------------------------------------------")

    def add_organelle(self, organelle):
        self.organelles.append(organelle)
        print(f" [SYSTEM] New organelle added   : {organelle.name}")

    def life_cycle(self):
        if not self.is_alive:
            print("[DEAD] Cell is dead.")
            return

        print(f"\n--- CYCLE START (ATP: {self.atp_storage} | Protein: {self.protein_stock}) ---")
        
        for organelle in self.organelles:
            organelle.operate(self)
            
        
        self.check_vital_signs()
        print("--- CYCLE END ---")

    def check_vital_signs(self):
        if self.atp_storage <= 0:
            self.is_alive = False
            print("\n!!! CRITICAL FAILURE: STARVATION. CELL DIED. !!!")
