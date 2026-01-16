# 1. Import pandas and create a DataFrame with columns: Name, Age, Marks.
# Display the first 5 rows and dataset shape.


import pandas as pd

df = pd.DataFrame({
    "Name": ["Amit", "Bibek", "rita", "dinesh", "bina", "rohit"],
    "Age": [18, 19, 20, 21, 22, 23],
    "Marks": [55, 67, 72, 80, 60, 90]
})

df.head()
df.shape
