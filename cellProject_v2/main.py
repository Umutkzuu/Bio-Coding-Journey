from cellV2 import Cell
import time

def main():
    print("Initializing Advanced Eukaryotic Cell Simulation...")
    my_cell = Cell("AGTC")

    
    for i in range(1, 11):
        print(f"\n>>> CYCLE {i} <<<")
        my_cell.life_cycle()
        
        
        time.sleep(1) 
        
        if not my_cell.is_alive:
            break

    print("\nSimulation Finished.")

if __name__ == "__main__":
    main()