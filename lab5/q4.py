# 4. Check for missing values in the dataset.
# Fill missing numerical values with the mean.

df.isna().sum()

df.fillna(df.mean(numeric_only=True), inplace=True)
