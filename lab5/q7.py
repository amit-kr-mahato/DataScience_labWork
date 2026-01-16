
# 7. Create a new column by transforming Marks (e.g., Marks / 10).
# Rename columns and save the cleaned dataset to a CSV file.


df["Marks_scaled"] = df["Marks"] / 10

df.rename(columns={"Marks": "Final_Marks"}, inplace=True)

df.to_csv("cleaned_data.csv", index=False)
