import pandas as pd

data = pd.read_csv("study_sessions.csv")
# print(data.head())
# print(data.shape)
# print(data.dtypes)
# print(data.columns)
# print(type(data["topic"]))
# print(type(data[["topic"]]))
mask = data["duration_minutes"] >= 100
total = data["duration_minutes"].sum()
mean = data["duration_minutes"].mean()
print("total    : ",total)
print("mean    : ",mean)
filtered_data = data[mask]

print(filtered_data)
print(mask.sum())
topic_counts = data["topic"].value_counts()

print(topic_counts)