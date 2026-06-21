import pandas as pd
import matplotlib.pyplot as plt
class CreditGate:
    def __init__(self,status,credit_score):
        self.status = str(status).strip().lower()
        self.credit_score = credit_score
    def pemeriksaan(self):
        if self.status == "aktif" and self.credit_score > 70:
            return "DISETUJUI"
        else:
            return "DITOLAK"


df = pd.read_csv("raw.csv")
new_df = df.copy()

new_df["Jumlah Pengajuan"] = new_df["Jumlah Pengajuan"].str.replace("Rp","").str.replace(".","")
new_df["Jumlah Pengajuan"] = pd.to_numeric(new_df["Jumlah Pengajuan"])
fil_na = new_df["Jumlah Pengajuan"].mean()
new_df["Jumlah Pengajuan"] = new_df["Jumlah Pengajuan"].fillna(fil_na)

print("=======================================================")
print(new_df.head(10))
print("=======================================================")


mask = (
    (new_df["Credit Score"] > 70) &
    (new_df["Status Pinjaman Sebelumnya"] == "Aktif")
)

new_df["Status Kelayakan"] = "DITOLAK"
new_df.loc[mask,"Status Kelayakan"] = "DISETUJUI"


print("=======================================================")
print(new_df.head(10))
print("=======================================================")

grup_credit = new_df.groupby("Status Kelayakan")["Credit Score"].mean()
grup_sum = new_df.groupby("Status Kelayakan")["Jumlah Pengajuan"].sum()

tes1 = CreditGate("aktif",10)
print(tes1.pemeriksaan())
print(grup_credit)
print(grup_sum)

new_df["Credit Score"].plot(
    kind="hist",
    bins=3
)

plt.title("Rata-rata Credit Score")
plt.xlabel("Credit Score")

plt.show()

plt.scatter(new_df["Jumlah Pengajuan"],new_df["Credit Score"])

plt.title("Rata-rata Credit Score")
plt.ylabel("Credit Score")
plt.xlabel("jumlah pengajuan")

plt.show()
