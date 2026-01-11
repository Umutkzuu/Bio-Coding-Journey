class Organelle:   

    def __init__(self, name, ):
        self.name = name

    def operate(self, cell):
        pass

    def __str__(self):
        return f"[{self.name}]"
    
class Mithochondria(Organelle): 

    def __init__(self):
        super().__init__("Mithochondria")

    def operate(self, cell):
        production_amount = 10
        cell.atp_storage += production_amount
        print(f" -> {self} Respiration done. +{production_amount} ATP")


class Ribosome(Organelle):

    def __init__(self):
            super().__init__("Ribosome")

    def operate(self, cell):
        energy_cost = 5
        if cell.atp_storage >= energy_cost:
            cell.atp_storage -= energy_cost
            cell.protein_stock += 1
            print(f" -> {self} Protein synthesis done. -{energy_cost} ATP,")

        else:
            print(f" -> {self} LOW ENERGY! Protein synthesis failed.")

class Lysosome(Organelle):
        def __init__(self):
            super().__init__("Lysosome")

        def operate(self, cell):
            if cell.waste_amount > 0 :
                cleaned = 2 
                cell.waste_amount -= cleaned
                print(f" -> {self} Waste digested. -{cleaned} Waste") 

            else:
                print(f" -> {self} No waste detected.")

class Nucleus(Organelle):
    def __init__(self, dna_code):
        super().__init__("Nucleus")
        self.dna_code = dna_code

    def operate(self, cell):
        print(f" -> {self} Managing DNA: {self.dna_code}...")


            
            