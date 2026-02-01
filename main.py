
import argparse
from src.config import SimulationConfig
from src.market import MinorityGameEngine
from src.analytics import generate_report

if __name__ == "__main__":
    conf = SimulationConfig()
    print(f"--- WIDS QUANT ENGINE STARTED (N={conf.N_AGENTS}) ---")
    
    engine = MinorityGameEngine(conf)
    for i in range(conf.STEPS):
        engine.step()
        
    generate_report(engine, "data/final_report.png")
    print("Simulation Complete.")
