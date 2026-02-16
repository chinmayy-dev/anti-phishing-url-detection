import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("data/dataset_schema_v1.csv")

# for shuffling
# df= df.sample(frac=1, random_state=42).reset_index(drop=True)
# df.to_csv("data/dataset_schema_v1.csv", index=False)

print(df.head())
print("\nDataset shape: ", df.shape)
print("\nColumn names: ", df.columns)
print("\nSummary statistics: \n", df.describe())
print("\nMean values by label: \n")
print(df.groupby("label").mean())

print(df.sort_values("url_length", ascending=False).head())


df[df["label"] == 0]["dot_count"].hist(alpha = 0.5, label = "Legit")
df[df["label"] == 1]["dot_count"].hist(alpha = 0.5, label = "Phishing")
plt.legend()
plt.title("Dot Count Distribution")
plt.show()

df[df["label"] == 0]["entropy"].hist(alpha = 0.5, label = "Legit")
df[df["label"] == 1]["entropy"].hist(alpha = 0.5, label = "Phishing")
plt.legend()
plt.title("Entropy Distribution")
plt.show()