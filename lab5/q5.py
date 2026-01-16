# 5. Detect duplicate rows in the dataset.
# Remove duplicates and verify the result.

df.duplicated()

df = df.drop_duplicates()
df.duplicated().sum()
