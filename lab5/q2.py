# 2. Load a CSV file into a DataFrame.
# Display column names, data types, and basic statistics.

df = pd.read_csv("data.csv")

df.columns
df.dtypes
df.describe()
