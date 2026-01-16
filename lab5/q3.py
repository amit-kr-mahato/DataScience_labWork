# 3. Select rows where Marks > 60.
# Select only Name and Marks columns.

df[df["Marks"] > 60][["Name", "Marks"]]
