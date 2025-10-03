import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(page_title="Compressor Analytics Dashboard", layout="wide")
st.title("🔧 Compressor Analytics Dashboard - Rashmi Metaliks")

# Sidebar filters
with st.sidebar:
    st.header("🔍 Filters")
    selected_date = st.date_input("Select Date", datetime.today())
    start_hour = st.slider("Start Hour", 0, 23, 0)
    end_hour = st.slider("End Hour", 0, 23, 23)

# Generate time index with 15-minute granularity
start_time = datetime.combine(selected_date, datetime.min.time()) + timedelta(hours=start_hour)
end_time = datetime.combine(selected_date, datetime.min.time()) + timedelta(hours=end_hour)
time_index = pd.date_range(start=start_time, end=end_time, freq='15T')
data_length = len(time_index)

# Seed for reproducibility
np.random.seed(selected_date.day + selected_date.month + selected_date.year)

# Simulated data
compressor_power = np.random.normal(loc=180, scale=20, size=data_length)  # kW
compressor_cfm = np.random.normal(loc=950, scale=30, size=data_length)    # CFM
rated_cfm = 1000

# Specific Energy Consumption (kW/CFM)
sec = compressor_power / compressor_cfm

# Create DataFrame
df = pd.DataFrame({
    'Time': time_index,
    'Power_kW': compressor_power,
    'CFM': compressor_cfm,
    'SEC_kW_per_CFM': sec
})
df.set_index('Time', inplace=True)

# KPI Cards
avg_power = df['Power_kW'].mean()
avg_cfm = df['CFM'].mean()
avg_sec = df['SEC_kW_per_CFM'].mean()
std_dev_cfm = np.std(df['CFM'] - rated_cfm)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Avg Compressor Power (kW)", f"{avg_power:.2f}")
col2.metric("Avg CFM", f"{avg_cfm:.2f}")
col3.metric("Avg kW/CFM", f"{avg_sec:.4f}")
col4.metric("Std Dev from Rated CFM", f"{std_dev_cfm:.2f}")

# Main Chart: Compressor Specific Energy Consumption Trend
fig1, ax1 = plt.subplots(figsize=(12, 5))
ax1.plot(df.index, df['SEC_kW_per_CFM'], color='orange', linewidth=2)
ax1.set_title("Compressor Specific Energy Consumption Trend")
ax1.set_xlabel("Timestamp")
ax1.set_ylabel("kW/CFM")
ax1.set_xticks(df.index[::max(1, len(df)//12)])
ax1.set_xticklabels([ts.strftime('%d %b (%H:%M)') for ts in df.index[::max(1, len(df)//12)]], rotation=45)
ax1.grid(True, linestyle='--', alpha=0.5)
st.pyplot(fig1)
fig1.savefig("compressor_sec_trend.png")

# Simulated Energy Loss Data (kWh)
energy_loss = np.random.normal(loc=50, scale=10, size=data_length)
df_loss = pd.DataFrame({
    'Time': time_index,
    'Energy_Loss_kWh': energy_loss
})
df_loss.set_index('Time', inplace=True)

# Cost Calculations
unit_cost = 4.2  # Rs/kWh
total_loss_kWh = df_loss['Energy_Loss_kWh'].sum()
total_cost_loss = total_loss_kWh * unit_cost

col5, col6 = st.columns(2)
col5.metric("Avg Energy Loss (kWh)", f"{df_loss['Energy_Loss_kWh'].mean():.2f}")
col6.metric("Total Cost of Power Loss (Rs)", f"{total_cost_loss:.2f}")

# Energy Loss Trend Chart
fig2, ax2 = plt.subplots(figsize=(12, 5))
ax2.plot(df_loss.index, df_loss['Energy_Loss_kWh'], color='red', linewidth=2)
ax2.set_title("Energy Loss Trend")
ax2.set_xlabel("Timestamp")
ax2.set_ylabel("Energy Loss (kWh)")
ax2.set_xticks(df_loss.index[::max(1, len(df_loss)//12)])
ax2.set_xticklabels([ts.strftime('%d %b (%H:%M)') for ts in df_loss.index[::max(1, len(df_loss)//12)]], rotation=45)
ax2.grid(True, linestyle='--', alpha=0.5)
st.pyplot(fig2)
fig2.savefig("energy_loss_trend.png")

# Create requirements.txt
with open("requirements.txt", "w") as f:
    f.write("streamlit\nmatplotlib\npandas\nnumpy")
