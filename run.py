import os
import pandas as pd
import matplotlib.pyplot as plt

# Input and output directories.
input_dir = 'original_data'
output_dir = 'converted_data'
if not os.path.exists(output_dir): os.makedirs(output_dir)

# Load original data.
input_file = os.path.join(input_dir, 'nyc_taxi_30m.csv')
df_30m = pd.read_csv(input_file, parse_dates=[0])
df_30m = df_30m.set_index('timestamp', drop=True)

# Re-sample original data.
df_42m = df_30m.resample('42Min').mean()
df_42m55s = df_30m.resample('42Min55s').mean()
df_1h = df_30m.resample('1H').mean()

# Load data aggregated by NuPIC and keep only columns 'timestamp' and 'value'.
input_file = os.path.join(input_dir, 'nyc_taxi_nupic_aggregated.csv')
df_nupic_42m55s = pd.read_csv(input_file, parse_dates=[0])
df_nupic_42m55s = df_nupic_42m55s.set_index('timestamp', drop=True)
for c in ['metric_value', 'anomaly_level', 'raw_anomaly_score']:
  if c in df_nupic_42m55s.columns.values:
    if c == 'metric_value': df_nupic_42m55s['value'] = df_nupic_42m55s[c]
    df_nupic_42m55s = df_nupic_42m55s.drop(c, 1)

# Save data.
df_42m.to_csv(os.path.join(output_dir, 'nyc_taxi_42m.csv'))
df_42m55s.to_csv(os.path.join(output_dir, 'nyc_taxi_42m55s.csv'))
df_1h.to_csv(os.path.join(output_dir, 'nyc_taxi_1h.csv'))
df_nupic_42m55s.to_csv(os.path.join(output_dir, 'nyc_taxi_nupic_42m55s.csv'))

# Plot data.
f, ax = plt.subplots()
ax.plot(df_30m.index, df_30m.value, marker='o', label='30m')
ax.plot(df_1h.index, df_1h.value, marker='o', label='1H')
ax.plot(df_42m.index, df_42m.value, marker='o', label='42m')
ax.plot(df_42m55s.index, df_42m55s.value, marker='o', label='42m55s')
ax.plot(df_nupic_42m55s.index, df_nupic_42m55s.value, marker='o',
        label='nupic_42m55s')
ax.legend()
plt.show()
