
from dataclasses import dataclass

@dataclass
class SimulationConfig:
    # --- Market Physics (Guaranteed Efficiency) ---
    N_AGENTS: int = 101           # Classic population size
    MEMORY_SIZE: int = 10         # m=10 (1024 patterns) >> 101 agents. No crowding.
    STEPS: int = 1500             # Longer runtime to let agents learn
    STRATEGIES_PER_AGENT: int = 20
    
    # --- Demographics ---
    # PURE SETUP: Smart Agents vs Random Noise
    # We removed Trend Traders because they cause artificial crashes.
    PCT_NOISE: float = 0.30       
    PCT_TREND: float = 0.00       # <--- SET TO ZERO TO STOP CRASHES
    PCT_SMART: float = 0.70       

    RANDOM_SEED: int = 555
    OUTPUT_DIR: str = "data/"
