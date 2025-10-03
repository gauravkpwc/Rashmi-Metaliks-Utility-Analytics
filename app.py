import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Set page config
st.set_page_config(page_title="Utility Analytics Visuals", layout="wide")

st.title("Analytics Visuals for Utility Systems")

# -------------------------------
# 1. Predictive Analytics Illustration
# -------------------------------
st.subheader("1. Predictive Analytics: Flue Gas Ratio Trend with Anomalies")

np.random.seed(0)
days = pd.date_range(start="2023-01-01", periods=30)
flue_gas_ratio = np.random.normal(loc=8, scale=0.5, size=30)
anomalies = [5, 12, 20]

fig1, ax1 = plt.subplots(figsize=(8, 4))
ax1.plot(days, flue_gas_ratio, label='Flue Gas Ratio', color='gray')
ax1.scatter(days[anomalies], flue_gas_ratio[anomalies], color='orange', label='Anomalies', zorder=5)
ax1.set_title("Flue Gas Ratio Trend with Anomalies")
ax1.set_xlabel("Date")
ax1.set_ylabel("Flue Gas Ratio")
plt.xticks(rotation=45)
ax1.legend()
st.pyplot(fig1)

# Save chart
fig1.savefig("predictive_analytics_flue_gas.png")

# -------------------------------
# 2. Heat Map: Energy Loss Across Utilities
# -------------------------------
st.subheader("2. Heat Map: Energy Loss Across Utilities")

utilities = ['Compressor', 'Boiler', 'Rolling Mill', 'Cooling Tower', 'Furnace']
loss_percent = [12, 18, 25, 10, 20]
heatmap_data = pd.DataFrame(np.array(loss_percent).reshape(1, -1), columns=utilities)

fig2, ax2 = plt.subplots(figsize=(8, 2))
sns.heatmap(heatmap_data, annot=True, cmap="OrRd", cbar=False, fmt="d", ax=ax2)
ax2.set_title("Energy Loss Across Utilities (%)")
ax2.set_yticks([])
st.pyplot(fig2)

# Save chart
fig2.savefig("energy_loss_heatmap.png")

# -------------------------------
# 3. Compressor Efficiency Trend
# -------------------------------
st.subheader("3. Compressor Efficiency Trend")

efficiency = np.random.normal(loc=85, scale=2, size=30)

fig3, ax3 = plt.subplots(figsize=(8, 4))
ax3.plot(days, efficiency, marker='o', linestyle='-', color='steelblue')
ax3.set_title("Compressor Efficiency Trend")
ax3.set_xlabel("Date")
ax3.set_ylabel("Efficiency (%)")
plt.xticks(rotation=45)
st.pyplot(fig3)

# Save chart
fig3.savefig("compressor_efficiency_trend.png")

st.success("Charts generated and saved as PNG files!")
