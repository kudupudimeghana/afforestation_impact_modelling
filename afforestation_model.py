import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# --- PARAMETERS ---
years = list(range(1, 21))  # 1 to 20 years
planted_trees = 1000
survival_rate_per_year = np.linspace(1.0, 0.9, len(years))  # from 100% to 90% survival

# --- Sample Tree Biomass Growth (Teak) ---
biomass_reference_years = [1, 5, 10, 15, 20]
biomass_values = [2, 25, 60, 100, 150]  # kg per tree

# Interpolate biomass for each year
biomass_per_tree = np.interp(years, biomass_reference_years, biomass_values)

# Carbon = 50% of biomass; CO₂ = Carbon * 3.67
carbon_per_tree = biomass_per_tree * 0.5
co2_per_tree = carbon_per_tree * 3.67

# Adjust for tree survival and number planted
trees_alive = planted_trees * survival_rate_per_year
co2_total = co2_per_tree * trees_alive

# --- Create DataFrame for Table ---
df = pd.DataFrame({
    "Year": years,
    "Biomass per Tree (kg)": np.round(biomass_per_tree, 2),
    "CO₂ per Tree (kg)": np.round(co2_per_tree, 2),
    "Trees Alive": np.round(trees_alive).astype(int),
    "Total CO₂ Sequestered (kg)": np.round(co2_total, 2)
})

print(df.to_string(index=False))

# --- Plot ---
plt.figure(figsize=(10, 5))
plt.plot(years, co2_total, marker='o', color='forestgreen')
plt.title(f"Total CO₂ Sequestered by {planted_trees} Teak Trees (with 90% Survival Rate)")
plt.xlabel("Year")
plt.ylabel("Total CO₂ Sequestered (kg)")
plt.grid(True)
plt.tight_layout()
plt.show()
