import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Set page config
st.set_page_config(page_title="Utility Analytics Dashboard", layout="wide")

st.title("Utility Analytics Dashboard")

# -------------------------------
# 1. Predictive Analytics: Flue Gas Ratio Trend with Anomalies
# -------------------------------
st.header("1. Predictive Analytics: Flue Gas Ratio")

np.random.seed(0)
days = pd.date_range(start="2023-01-01", periods=30)
flue_gas_ratio = np.random.normal(loc=8, scale=0.5, size=30)
anomalies = [5, 12, 20]
standard_flue_gas_ratio = 8

avg_flue_gas = np.mean(flue_gas_ratio)
deviation_flue_gas = avg_flue_gas - standard_flue_gas_ratio

col1, col2 = st.columns(2)
col1.metric("Average Flue Gas Ratio", f"{avg_flue_gas:.2f}")
col2.metric("Deviation from Standard", f"{deviation_flue_gas:.2f}")

fig1, ax1 = plt.subplots(figsize=(8, 4))
ax1.plot(days, flue_gas_ratio, label='Flue Gas Ratio', color='gray')
ax1.scatter(days[anomalies], flue_gas_ratio[anomalies], color='orange', label='Anomalies', zorder=5)
ax1.set_title("Flue Gas Ratio Trend with Anomalies")
ax1.set_xlabel("Date")
ax1.set_ylabel("Flue Gas Ratio")
plt.xticks(rotation=45)
ax1.legend()
st.pyplot(fig1)
fig1.savefig("predictive_analytics_flue_gas.png")

# -------------------------------
# 2. Line Trend: Energy Loss Across Utilities Over Time
# -------------------------------
st.header("2. Energy Loss Trend Across Utilities")

# Generate timestamps with 15-minute granularity
timestamps = pd.date_range(start="2023-01-01 00:00", periods=96, freq="15min")
utilities = ['Compressor', 'Boiler', 'Rolling Mill', 'Cooling Tower', 'Furnace']

# Simulate energy loss data
energy_loss_df = pd.DataFrame({
    'Timestamp': timestamps,
    'Compressor': np.random.normal(loc=12, scale=2, size=96),
    'Boiler': np.random.normal(loc=18, scale=2, size=96),
    'Rolling Mill': np.random.normal(loc=25, scale=2, size=96),
    'Cooling Tower': np.random.normal(loc=10, scale=2, size=96),
    'Furnace': np.random.normal(loc=20, scale=2, size=96),
})

energy_loss_df['Formatted Time'] = energy_loss_df['Timestamp'].dt.strftime('%d %b (%H:%M)')

fig2, ax2 = plt.subplots(figsize=(10, 5))
for utility in utilities:
    ax2.plot(energy_loss_df['Formatted Time'], energy_loss_df[utility], label=utility)
ax2.set_title("Energy Loss Trend Across Utilities")
ax2.set_xlabel("Timestamp")
ax2.set_ylabel("Energy Loss (%)")
plt.xticks(rotation=45)
ax2.legend()
st.pyplot(fig2)
fig2.savefig("energy_loss_trend.png")

# -------------------------------
# 3. Compressor Efficiency Trend
# -------------------------------
st.header("3. Compressor Efficiency Trend")

efficiency = np.random.normal(loc=85, scale=2, size=30)
actual_cfm = np.random.normal(loc=980, scale=20, size=30)
rated_cfm = 1000

avg_efficiency = np.mean(efficiency)
avg_actual_cfm = np.mean(actual_cfm)
std_dev_cfm = np.std(actual_cfm - rated_cfm)

col3, col4, col5 = st.columns(3)
col3.metric("Average Efficiency (%)", f"{avg_efficiency:.2f}")
col4.metric("Avg Actual CFM vs Rated", f"{avg_actual_cfm:.2f} / {rated_cfm}")
col5.metric("Std Dev of CFM from Rated", f"{std_dev_cfm:.2f}")

fig3, ax3 = plt.subplots(figsize=(8, 4))
ax3.plot(days, efficiency, marker='o', linestyle='-', color='steelblue')
ax3.set_title("Compressor Efficiency Trend")
ax3.set_xlabel("Date")
ax3.set_ylabel("Efficiency (%)")
plt.xticks(rotation=45)
st.pyplot(fig3)
fig3.savefig("compressor_efficiency_trend.png")

# -------------------------------
# Create requirements.txt
# -------------------------------
with open("requirements.txt", "w") as f:
    f.write("streamlit\nmatplotlib\nseaborn\npandas\nnumpy")
