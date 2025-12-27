import pandas as pd
import numpy as np

np.random.seed(42)
rows = 650

data = {
    "CustomerID": range(1001, 1001 + rows),
    "Age": np.random.randint(18, 70, rows),
    "Gender": np.random.choice(["Male", "Female","other"], rows),
    "AnnualIncome": np.random.randint(20000, 120000, rows),
    "SpendingScore": np.random.randint(1, 100, rows),
    "Region": np.random.choice(["North", "South", "East", "West"], rows),
    "Purchased": np.random.choice([0, 1], rows)
}

df = pd.DataFrame(data)

# Introduce missing values
for col in ["Age", "AnnualIncome", "SpendingScore"]:
    df.loc[df.sample(frac=0.08).index, col] = np.nan

# Introduce outliers
df.loc[df.sample(10).index, "AnnualIncome"] = df["AnnualIncome"] * 5
df.loc[df.sample(8).index, "Age"] = 120

df.to_csv("/home/network/project/eda_customer_project/data/raw_customer_data.csv", index=False)
print("✅ raw_customer_data.csv generated with missing values & outliers")