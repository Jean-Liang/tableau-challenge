import pandas as pd

# Load the two CSV files
file_path_1 = '202401-citibike-tripdata_1.csv'
file_path_2 = '202401-citibike-tripdata_2.csv'

df1 = pd.read_csv(file_path_1)
df2 = pd.read_csv(file_path_2)

# Combine the datasets
combined_df = pd.concat([df1, df2], ignore_index=True)

# Save the combined dataset to a CSV file
combined_csv_path = '202401-citibike-tripdata.csv'
combined_df.to_csv(combined_csv_path, index=False)

print(f"Combined data saved to {combined_csv_path}")