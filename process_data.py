import pandas as pd

# Load CSV files
df1 = pd.read_csv("data/daily_sales_data_0.csv")
df2 = pd.read_csv("data/daily_sales_data_1.csv")
df3 = pd.read_csv("data/daily_sales_data_2.csv")

# Combine all data
df = pd.concat([df1, df2, df3])

# 🔹 Clean Data

# Convert price to float
df['price'] = df['price'].replace(r'[\$,]', '', regex=True).astype(float)

# Convert date to datetime
df['date'] = pd.to_datetime(df['date'])

# 🔹 Filter only Pink Morsel
df = df[df['product'] == 'pink morsel']

# 🔹 Create sales column
df['sales'] = df['price'] * df['quantity']

# 🔹 Select required columns
final_df = df[['sales', 'date', 'region']]

# 🔹 Save output file
final_df.to_csv("processed_data.csv", index=False)

print("✅ Data processed successfully!")
print(final_df.head())