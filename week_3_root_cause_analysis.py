import pandas as pd
import numpy as np

# 1. Enhanced Ingestion Dataset with Root Cause Tracking
data = {
    'Day': [1, 5, 10, 14, 15],
    'Total_Transactions': [10450, 11200, 10890, 12050, 11900],
    'Error_Count': [145, 162, 155, 220, 275],
    'Primary_Root_Cause': ['None', 'None', 'None', 'Network Latency', 'API Gateway Timeout']
}

df = pd.DataFrame(data)

# 2. Recalculate Defect Rates & Control Metrics
df['Defect_Rate_Pct'] = round((df['Error_Count'] / df['Total_Transactions']) * 100, 2)
baseline_mean = 1.45
std_dev = 0.22
ucl = round(baseline_mean + (3 * std_dev), 2)

# 3. Validated Status Evaluation
df['Validation_Status'] = np.where(df['Defect_Rate_Pct'] > ucl, 'Confirmed Breach (Root Cause Identified)', 'Normal')

# 4. Output Validation Summary
print("--- WEEK 3 ROOT CAUSE STUDY & VALIDATION ---")
print(f"Control Threshold UCL: {ucl}%\n")
print(df[['Day', 'Total_Transactions', 'Error_Count', 'Defect_Rate_Pct', 'Primary_Root_Cause', 'Validation_Status']].to_string(index=False))
