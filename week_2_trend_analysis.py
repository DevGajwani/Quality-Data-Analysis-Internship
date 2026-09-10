import pandas as pd
import numpy as np

# 1. Create the dataset matching the Week 2 report parameters
data = {
    'Day': [1, 5, 10, 14, 15],
    'Total_Transactions': [10450, 11200, 10890, 12050, 11900],
    'Error_Count': [145, 162, 155, 220, 275]
}

df = pd.DataFrame(data)

# 2. Calculate Defect Rate (%)
df['Defect_Rate_Pct'] = round((df['Error_Count'] / df['Total_Transactions']) * 100, 2)

# 3. Establish Baseline SPC Metrics
baseline_mean = 1.45
std_dev = 0.22
ucl = round(baseline_mean + (3 * std_dev), 2)

# 4. Evaluate SPC Anomalies against Control Limits
df['Status'] = np.where(df['Defect_Rate_Pct'] > ucl, 'Anomaly (Breach)', 
               np.where(df['Defect_Rate_Pct'] >= 1.82, 'Warning', 'Normal'))

# 5. Output Results
print("--- QUALITY DEFECT RATE TREND ANALYSIS ---")
print(f"Baseline Mean: {baseline_mean}%")
print(f"Standard Deviation: {std_dev}%")
print(f"Upper Control Limit (UCL): {ucl}%\n")
print(df.to_string(index=False))
