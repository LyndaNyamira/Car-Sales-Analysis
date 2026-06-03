import pandas as pd

file_path = "C:\\Users\\lynda\\Documents\\School\\Master of IT\\T2 24\\Data analytics\\Assessment 2\\Car sales\\car_prices.csv"
df = pd.read_csv(file_path)

df_cleaned = df.dropna()

df_sample = df_cleaned.sample(n=5000, random_state=42)

output_file_path = "C:\\Users\\lynda\\Documents\\School\\Master of IT\\T2 24\\Data analytics\\Assessment 2\\Car sales\\car_prices_sample.csv"
df_sample.to_csv(output_file_path, index=False)

print(f"Sampled data saved to {output_file_path}")
