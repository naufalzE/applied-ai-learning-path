import requests

def fetch_data(url):

    response = requests.get(
        url,
        timeout=5
    )

    if response.status_code == 200:
        return response.json()

    return None


url = "https://jsonplaceholder.typicode.com/users/1"

data = fetch_data(url)

try:
    print(f"Nama    : {data["name"]}")
except:
    print("Data tidak ditemukan")
if data != None:
    print(f"Nama    : {data["name"]}")
else:
    print("Data tidak ditemukan")