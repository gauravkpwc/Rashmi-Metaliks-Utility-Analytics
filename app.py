import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(page_title="Compressor Analytics Dashboard", layout="wide")
st.markdown("<h1 style='text-align: center;'>🔧 Compressor Analytics Dashboard - Rashmi Metaliks</h1>", unsafe_allow_html=True)

# Sidebar filters
with st.sidebar:
    st.header("🔍 Filters")
    selected_date = st.date_input("Select Date", datetime.today())
    start_hour = st.slider("Start Hour", 0, 23, 0)
    end_hour = st.slider("End Hour", 0, 23, 23)
    departments = ['Sintering', 'Pelletizing', 'DRI', 'BF']
    selected_departments = st.multiselect("Select Departments", departments, default=departments)
    equipment_map = {
        'Sintering': ['Conveyor', 'Blower', 'Heater', 'Compressor', 'Pump', 'Burner'],
        'Pelletizing': ['Conveyor', 'Blower', 'Dryer', 'Compressor', 'Pump', 'Mixer'],
        'DRI': ['Conveyor', 'Blower', 'Reactor', 'Compressor', 'Pump', 'Cooler'],
        'BF': ['Conveyor', 'Blower', 'Stove', 'Compressor', 'Pump', 'Crane']
    }
    selected_unit = selected_departments[0] if len(selected_departments) == 1 else st.selectbox("Select Unit for Equipment View", selected_departments)
    selected_equipment = st.selectbox("Select Equipment", ["All"] + equipment_map.get(selected_unit, []))

# Generate time index with 15-minute granularity
start_time = datetime.combine(selected_date, datetime.min.time()) + timedelta(hours=start_hour)
end_time = datetime.combine(selected_date, datetime.min.time()) + timedelta(hours=end_hour)
time_index = pd.date_range(start=start_time, end=end_time, freq='15T')
data_length = len(time_index)

# Seed for reproducibility
np.random.seed(selected_date.day + selected_date.month + selected_date.year)

# Simulated compressor data
compressor_power = np.random.normal(loc=180, scale=20, size=data_length)  # kW
compressor_cfm = np.random.normal(loc=950, scale=30, size=data_length)    # CFM
rated_cfm = 1000
sec = compressor_power / compressor_cfm

df = pd.DataFrame({
    'Time': time_index,
    'Power_kW': compressor_power,
    'CFM': compressor_cfm,
    'SEC_kW_per_CFM': sec
})
df.set_index('Time', inplace=True)

# KPI calculations
avg_power = df['Power_kW'].mean()
avg_cfm = df['CFM'].mean()
avg_sec = df['SEC_kW_per_CFM'].mean()
std_dev_cfm = np.std(df['CFM'] - rated_cfm)

# KPI Cards
card_style = "background-color:#FFE5CC; padding:10px; border-radius:8px; text-align:center; font-size:18px; font-weight:bold;"
col1, col2, col3, col4 = st.columns(4)
col1.markdown(f"<div style='{card_style}'>⚡ Avg Power (kW)<br>{avg_power:,.1f}</div>", unsafe_allow_html=True)
col2.markdown(f"<div style='{card_style}'>💨 Avg CFM<br>{avg_cfm:,.1f}</div>", unsafe_allow_html=True)
col3.markdown(f"<div style='{card_style}'>🔧 Avg kW/CFM<br>{avg_sec:,.3f}</div>", unsafe_allow_html=True)
col4.markdown(f"<div style='{card_style}'>📊 Std Dev from Rated CFM<br>{std_dev_cfm:,.1f}</div>", unsafe_allow_html=True)

# Main Chart: Compressor SEC Trend
fig1, ax1 = plt.subplots(figsize=(12, 5))
ax1.plot(df.index, df['SEC_kW_per_CFM'], color='#FD5108', linewidth=2)
ax1.set_title("Compressor Specific Energy Consumption Trend")
ax1.set_xlabel("Timestamp")
ax1.set_ylabel("kW/CFM")
ax1.set_xticks(df.index[::max(1, len(df)//12)])
ax1.set_xticklabels([ts.strftime('%d %b (%H:%M)') for ts in df.index[::max(1, len(df)//12)]], rotation=45)
ax1.grid(True, linestyle='--', alpha=0.5)
st.pyplot(fig1)
fig1.savefig("compressor_sec_trend.png")

# Simulated Energy Loss Data
energy_loss = np.random.normal(loc=50, scale=10, size=data_length)
df_loss = pd.DataFrame({'Time': time_index, 'Energy_Loss_kWh': energy_loss})
df_loss.set_index('Time', inplace=True)

# Simulated equipment loss data
equipment_colors = ['#1f77b4', '#2ca02c', '#9467bd']  # blue, green, purple
equipment_names = ['Compressor', 'Pump', 'Blower']
for i, eq in enumerate(equipment_names):
    df_loss[eq] = np.random.normal(loc=15 + i*5, scale=5, size=data_length)

# Cost Calculations
unit_cost = 4.2
total_loss_kWh = df_loss['Energy_Loss_kWh'].sum()
avg_loss_kWh = df_loss['Energy_Loss_kWh'].mean()
total_cost_loss = total_loss_kWh * unit_cost

col5, col6, col7 = st.columns(3)
col5.markdown(f"<div style='{card_style}'>🔋 Total Energy Loss (kWh)<br>{total_loss_kWh:,.1f}</div>", unsafe_allow_html=True)
col6.markdown(f"<div style='{card_style}'>📉 Avg Energy Loss (kWh)<br>{avg_loss_kWh:,.1f}</div>", unsafe_allow_html=True)
col7.markdown(f"<div style='{card_style}'>💰 Total Cost Loss (Rs)<br>{total_cost_loss:,.1f}</div>", unsafe_allow_html=True)

# Energy Loss Trend Chart
fig2, ax2 = plt.subplots(figsize=(12, 5))
ax2.plot(df_loss.index, df_loss['Energy_Loss_kWh'], color='#4B4B4B', linewidth=2, label='Total Energy Loss')
for i, eq in enumerate(equipment_names):
    ax2.plot(df_loss.index, df_loss[eq], color=equipment_colors[i], linestyle='--', linewidth=2, label=f'{eq} Loss')
ax2.set_title("Energy Loss Trend")
ax2.set_xlabel("Timestamp")
ax2.set_ylabel("Energy Loss (kWh)")
ax2.set_xticks(df_loss.index[::max(1, len(df_loss)//12)])
ax2.set_xticklabels([ts.strftime('%d %b (%H:%M)') for ts in df_loss.index[::max(1, len(df_loss)//12)]], rotation=45)
ax2.grid(True, linestyle='--', alpha=0.5)
ax2.legend()
st.pyplot(fig2)
fig2.savefig("energy_loss_trend.png")

# Create requirements.txt
with open("requirements.txt", "w") as f:
    f.write("streamlit\nmatplotlib\npandas\nnumpy")
