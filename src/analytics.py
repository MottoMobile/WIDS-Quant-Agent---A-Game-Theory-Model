
import matplotlib.pyplot as plt
import pandas as pd

def generate_report(model, filename="simulation_report.png"):
    df = model.datacollector.get_model_vars_dataframe()
    
    fig, axes = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
    
    # Plot 1: Supply/Demand
    axes[0].plot(df["Buyers"], color='#34495e', lw=1, alpha=0.9)
    axes[0].axhline(model.conf.N_AGENTS/2, color='r', ls='--', label="Equilibrium")
    axes[0].set_title(f"Market Demand (N={model.conf.N_AGENTS})")
    axes[0].set_ylabel("Number of Buyers")
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)
    
    # Plot 2: Alpha
    axes[1].plot(df["Inefficiency_Alpha"], color='#8e44ad', lw=1.5)
    axes[1].axhline(1.0, color='g', ls=':', label="Random Walk (Alpha=1)")
    axes[1].set_title("Market Inefficiency (Alpha < 1 = Efficient)")
    axes[1].set_ylabel("Alpha")
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(filename)
    print(f">> Report saved to {filename}")
