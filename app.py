import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# -------------------------------
# 1. Predictive Analytics Illustration (Flue Gas Ratio Trend with anomalies)
# -------------------------------
np.random.seed(0)
days = pd.date_range(start="2023-01-01", periods=30)
flue_gas_ratio = np.random.normal(loc=8, scale=0.5, size=30)
anomalies = [5, 12, 20]  # indices of anomalies

plt.figure(figsize=(8, 4))
plt.plot(days, flue_gas_ratio, label='Flue Gas Ratio', color='gray')
plt.scatter(days[anomalies], flue_gas_ratio[anomalies], color='orange', label='Anomalies', zorder=5)
plt.title("Flue Gas Ratio Trend with Anomalies")
plt.xlabel("Date")
plt.ylabel("Flue Gas Ratio")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig("predictive_analytics_flue_gas.png")
plt.close()

# -------------------------------
# 2. Heat Map: Energy loss across utilities
# -------------------------------
utilities = ['Compressor', 'Boiler', 'Rolling Mill', 'Cooling Tower', 'Furnace']
loss_percent = [12, 18, 25, 10, 20]
heatmap_data = pd.DataFrame(np.array(loss_percent).reshape(1, -1), columns=utilities)

plt.figure(figsize=(8, 2))
sns.heatmap(heatmap_data, annot=True, cmap="OrRd", cbar=False, fmt="d")
plt.title("Energy Loss Across Utilities (%)")
plt.yticks([])
plt.tight_layout()
plt.savefig("energy_loss_heatmap.png")
plt.close()

# -------------------------------
# 3. Compressor Efficiency Trend
# -------------------------------
days = pd.date_range(start="2023-01-01", periods=30)
efficiency = np.random.normal(loc=85, scale=2, size=30)

plt.figure(figsize=(8, 4))
plt.plot(days, efficiency, marker='o', linestyle='-', color='steelblue')
plt.title("Compressor Efficiency Trend")
plt.xlabel("Date")
plt.ylabel("Efficiency (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("compressor_efficiency_trend.png")
plt.close()

# -------------------------------
# Create requirements.txt
# -------------------------------
with open("requirements.txt", "w") as f:
    f.write("matplotlib\nseaborn\npandas\nnumpy")
