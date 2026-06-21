data = {
    "duration": [
        100,
        None,
        50,
        None,
        150
    ]
}
import pandas as pd
# Tugas
# Buat DataFrame.
# Hitung jumlah missing value.
# Hitung mean duration.
# Isi NaN menggunakan mean.
# Tampilkan DataFrame hasil cleaning.
df = pd.DataFrame(data)

total_mising = df["duration"].isna().sum()
print(f"total mising    : {total_mising}")
mean_fill = df["duration"].mean()
print(f"rata rata   : {mean_fill}")
df["duration"] = df["duration"].fillna(mean_fill)
print(df)
