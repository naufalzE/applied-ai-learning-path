import requests

try:

    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/1",
        timeout=5
    )

    print(response.status_code)

except requests.ConnectionError:

    print("Koneksi gagal")
except requests.Timeout:
    print("TIME-OUT")