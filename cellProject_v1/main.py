from cell import Cell
from organelles import Ribosome 

def main():

    my_cell = Cell(dna_code = "AGTC-GATC-001")

    input ("Press Enter to run Cycle 1...")
    my_cell.life_cycle()

    input ("Press Enter to run Cycle 2...")
    my_cell.life_cycle()

    print("\n[EVENT] The cell needs more proteins! Adding extra Ribosomes...")
    my_cell.add_organelle(Ribosome())

    
    input("Press Enter to run Cycle 3 (With extra Ribosome)...")
    my_cell.life_cycle()

    print("\nSimulation Finished.")

if __name__ == "__main__":
    main()