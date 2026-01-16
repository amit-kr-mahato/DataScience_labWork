# 6. Identify outliers in the Marks column using the IQR method.
# Remove the outliers from the dataset.

Q1 = df["Marks"].quantile(0.25)
Q3 = df["Marks"].quantile(0.75)
IQR = Q3 - Q1

df = df[(df["Marks"] >= Q1 - 1.5 * IQR) & (df["Marks"] <= Q3 + 1.5 * IQR)]
