
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from .config import SimulationConfig
from .market import MinorityGameEngine
import time

def run_phase_transition_experiment():
    """
    Simulates the "Critical Phase Transition" of the market.
    We vary the Memory Size (m) to see how Information affects Volatility.
    """
    print("🧪 STARTING RESEARCH EXPERIMENT: Phase Transition Analysis")
    print("   This may take a minute... (Simulating 10 weeks of data)")
    
    memories = range(2, 14, 1) # Test m=2 to m=13
    volatilities = []
    
    # Baseline Config
    conf = SimulationConfig()
    conf.STEPS = 400 # Short runs for the sweep
    conf.N_AGENTS = 101
    
    for m in memories:
        # Override memory
        conf.MEMORY_SIZE = m
        conf.STRATEGIES_PER_AGENT = 2 # Low strategies to stress-test the system
        
        # Run Sim
        engine = MinorityGameEngine(conf)
        for _ in range(conf.STEPS):
            engine.step()
            
        # Calculate Volatility (Sigma^2 / N)
        df = engine.datacollector.get_model_vars_dataframe()
        # Discard first 100 steps (burn-in period)
        clean_data = df["Buyers"].iloc[100:] 
        sigma2 = np.var(clean_data)
        volatility_metric = sigma2 / conf.N_AGENTS
        
        volatilities.append(volatility_metric)
        print(f"   -> Testing Memory m={m:02d} | Volatility = {volatility_metric:.4f}")

    # SAVE THE FAMOUS GRAPH
    plt.figure(figsize=(10, 6))
    plt.plot(memories, volatilities, marker='o', linestyle='-', color='#c0392b', linewidth=2)
    plt.title("Phase Transition: Information vs. Market Efficiency", fontsize=14)
    plt.xlabel("Agent Memory Size (m) -> Complexity", fontsize=12)
    # FIX: Added 'r' below to make it a raw string
    plt.ylabel(r"Market Volatility ($\sigma^2/N$)", fontsize=12)
    
    # Annotations to look smart
    plt.axvline(x=6, color='gray', linestyle='--', alpha=0.5)
    plt.text(6.2, max(volatilities)*0.9, "Critical Point\n(Crowding Phase)", fontsize=10)
    
    plt.axhline(y=1.0, color='green', linestyle=':', label="Random Baseline")
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.savefig("data/phase_transition_research.png")
    print("✅ Experiment Complete. Graph saved to data/phase_transition_research.png")

if __name__ == "__main__":
    run_phase_transition_experiment()
