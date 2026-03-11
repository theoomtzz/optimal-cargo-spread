import matplotlib.pyplot as plt
import numpy as np
from optimal_pricing import price_return_optimal_price
from fixed_pricing import price_return_fixe_price

# Function to plot the comparison between fixed and optimal strategies
def drawn():
    WT = 0.1
    T = 30
    t = np.arange(0, 31)
    
    # Data retrieval
    Pfixstrat, Xfixstrat = price_return_fixe_price(WT, T)
    Poptistrat, Xoptistrat = price_return_optimal_price(WT, T)
    
    # --- Figure creation with 3 subplots (1 row, 3 columns) ---
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 5.5))

    # ==========================================
    # 1. PREMIUM Plot (Spread proposed)
    # ==========================================
    ax1.plot(t, Pfixstrat, color='#e74c3c', linestyle='-', linewidth=2.5, label='Premium (Fixed)')
    ax1.plot(t, Poptistrat, color='#2980b9', linestyle='-', linewidth=2.5, label='Premium (Optimal)')
    ax1.set_xlabel("Time t (Days elapsed)", fontsize=11)
    ax1.set_ylabel("Proposed Premium p(t)", fontsize=11)
    ax1.set_title("1. Premium Evolution (Spread)", fontsize=13, fontweight='bold')
    ax1.legend(loc='upper right')
    ax1.grid(True, linestyle='--', alpha=0.7)

    # ==========================================
    # 2. EXPECTED RETURN Plot
    # ==========================================
    ax2.plot(t, Xfixstrat, color='#e74c3c', linestyle='--', linewidth=2.5, label='Expected Return (Fixed)')
    ax2.plot(t, Xoptistrat, color='#2980b9', linestyle='--', linewidth=2.5, label='Expected Return (Optimal)')
    ax2.set_xlabel("Time t (Days elapsed)", fontsize=11)
    ax2.set_ylabel("Total Expected Wealth W(t)", fontsize=11)
    ax2.set_title("2. Expected Profit Evolution", fontsize=13, fontweight='bold')
    ax2.legend(loc='upper right')
    ax2.grid(True, linestyle='--', alpha=0.7)

    
    # ==========================================
    # 3. COMBINED Plot (Dual Axis)
    # ==========================================
    # Left Axis: Expected Return (dashed lines with transparency)
    ax3.plot(t, Xfixstrat, color='#e74c3c', linestyle='--', linewidth=2, alpha=0.6, label='Expected Return (Fixed)')
    ax3.plot(t, Xoptistrat, color='#2980b9', linestyle='--', linewidth=2, alpha=0.6, label='Expected Return (Optimal)')
    ax3.set_xlabel("Time t (Days elapsed)", fontsize=11)
    ax3.set_ylabel("Total Expected Wealth W(t)", color='black', fontsize=11)
    
    # Right Axis: Premium (solid lines)
    ax4 = ax3.twinx()
    ax4.plot(t, Pfixstrat, color='#e74c3c', linestyle='-', linewidth=2.5, label='Premium (Fixed)')
    ax4.plot(t, Poptistrat, color='#2980b9', linestyle='-', linewidth=2.5, label='Premium (Optimal)')
    ax4.set_ylabel("Proposed Premium p(t)", color='black', fontsize=11)
    
    ax3.set_title("3. Dynamic Synthesis (Dual Axis)", fontsize=13, fontweight='bold')
    
    # Merge legends for the combined plot
    lines_1, labels_1 = ax3.get_legend_handles_labels()
    lines_2, labels_2 = ax4.get_legend_handles_labels()
    ax4.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper left', fontsize=9)
    
    ax3.grid(True, linestyle='--', alpha=0.7)

    # --- Layout adjustment and saving ---
    plt.tight_layout() 
    
    # Save the plot in the same directory as the script
    plt.savefig("cargo_spread_plot.png", dpi=300, bbox_inches='tight')
    
    print("Plot successfully generated! Check the 'cargo_spread_plot.png' file.")
    
    # Keep show() to display it, image is saved regardless
    plt.show(block=True) 

    return

drawn()