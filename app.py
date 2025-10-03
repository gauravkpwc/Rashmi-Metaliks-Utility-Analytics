import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set page config
st.set_page_config(page_title="Utility Analytics Dashboard", layout="wide")

st.title("Utility Analytics Dashboard")

# -------------------------------
# Generate common timestamp axis
# -------------------------------
timestamps = pd.date_range(start="2023-01-01 00:00", periods=96, freq="15min")
formatted_time = timestamps.strftime('%d %b (%H:%M)')

# Sidebar filter
selected_date = st.sidebar.selectbox("Select Date", sorted(set(timestamps.date)))
mask = timestamps.date == selected_date
filtered_timestamps = timestamps[mask]
filtered_formatted_time = formatted_time[mask]

# -------------------------------
# 1. Predictive Analytics: Flue Gas Ratio
# -------------------------------
st.header("1. Predictive Analytics: Flue Gas Ratio")

np.random.seed(0)
flue_gas_ratio = np.random.normal(loc=8, scale=0.5, size=96)
flue_gas_ratio_filtered = flue_gas_ratio[mask]
anomalies = np.random.choice(np.where(mask)[0], size=3, replace=False)
standard_flue_gas_ratio = 8

avg_flue_gas = np.mean(flue_gas_ratio_filtered)
deviation_flue_gas = avg_flue_gas - standard_flue_gas_ratio

col1, col2 = st.columns(2)
col1.metric("Average Flue Gas Ratio", f"{avg_flue_gas:.2f}")
col2.metric("Deviation from Standard", f"{deviation_flue_gas:.2f}")

fig1, ax1 = plt.subplots(figsize=(10, 4))
ax1.plot(filtered_formatted_time, flue_gas_ratio_filtered, label='Flue Gas Ratio', color='gray')
ax1.scatter(formatted_time[anomalies], flue_gas_ratio[anomalies], color='orange', label='Anomalies', zorder=5)
ax1.set_title("Flue Gas Ratio Trend with Anomalies")
ax1.set_xlabel("Timestamp")
ax1.set_ylabel("Flue Gas Ratio")
ax1.set_xticks(filtered_formatted_time[::8])
ax1.tick_params(axis='x', rotation=45)
ax1.legend()
st.pyplot(fig1)
fig1.savefig("predictive_analytics_flue_gas.png")

# -------------------------------
# 2. Energy Loss Trend Across Utilities
# -------------------------------
st.header("2. Energy Loss Trend Across Utilities")

utilities = ['Compressor', 'Boiler', 'Rolling Mill', 'Cooling Tower', 'Furnace']
energy_loss_df = pd.DataFrame({
    'Timestamp': timestamps,
    'Compressor': np.random.normal(loc=12, scale=2, size=96),
    'Boiler': np.random.normal(loc=18, scale=2, size=96),
    'Rolling Mill': np.random.normal(loc=25, scale=2, size=96),
    'Cooling Tower': np.random.normal(loc=10, scale=2, size=96),
    'Furnace': np.random.normal(loc=20, scale=2, size=96),
})
energy_loss_filtered = energy_loss_df[energy_loss_df['Timestamp'].dt.date == selected_date]

avg_loss = energy_loss_filtered[utilities].mean().mean()
cost_loss_low = avg_loss * 1.2
cost_loss_high = avg_loss * 4.3

col3, col4, col5 = st.columns(3)
col3.metric("Average Energy Loss (%)", f"{avg_loss:.2f}")
col4.metric("Cost Loss @ ₹1.2/kWh", f"₹{cost_loss_low:.2f}")
col5.metric("Cost Loss @ ₹4.3/kWh", f"₹{cost_loss_high:.2f}")

fig2, ax2 = plt.subplots(figsize=(10, 5))
for utility in utilities:
    ax2.plot(filtered_formatted_time, energy_loss_filtered[utility].values, label=utility)
ax2.set_title("Energy Loss Trend Across Utilities")
ax2.set_xlabel("Timestamp")
ax2.set_ylabel("Energy Loss (%)")
ax2.set_xticks(filtered_formatted_time[::8])
ax2.tick_params(axis='x', rotation=45)
ax2.legend()
st.pyplot(fig2)
fig2.savefig("energy_loss_trend.png")

# -------------------------------
# 3. Compressor Efficiency Trend
# -------------------------------
st.header("3. Compressor Efficiency Trend")

efficiency = np.random.normal(loc=85, scale=2, size=96)
actual_cfm = np.random.normal(loc=980, scale=20, size=96)
rated_cfm = 1000

efficiency_filtered = efficiency[mask]
actual_cfm_filtered = actual_cfm[mask]

avg_efficiency = np.mean(efficiency_filtered)
avg_actual_cfm = np.mean(actual_cfm_filtered)
std_dev_cfm = np.std(actual_cfm_filtered - rated_cfm)

col6, col7, col8 = st.columns(3)
col6.metric("Average Efficiency (%)", f"{avg_efficiency:.2f}")
col7.metric("Avg Actual CFM vs Rated", f"{avg_actual_cfm:.2f} / {rated_cfm}")
col8.metric("Std Dev of CFM from Rated", f"{std_dev_cfm:.2f}")

fig3, ax3 = plt.subplots(figsize=(10, 4))
ax3.plot(filtered_formatted_time, efficiency_filtered, marker='o', linestyle='-', color='steelblue')
ax3.set_title("Compressor Efficiency Trend")
ax3.set_xlabel("Timestamp")
ax3.set_ylabel("Efficiency (%)")
ax3.set_xticks(filtered_formatted_time[::8])
ax3.tick_params(axis='x', rotation=45)
st.pyplot(fig3)
fig3.savefig("compressor_efficiency_trend.png")

# -------------------------------
# Create requirements.txt
# -------------------------------
with open("requirements.txt", "w") as f:
    f.write("streamlit\nmatplotlib\npandas\nnumpy")
