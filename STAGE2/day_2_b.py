import requests


def fetch_user(user_id):
    """
    Mengambil data user dari API.
    Mengembalikan structured response.
    """

    try:

        response = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{user_id}",
            timeout=5
        )

        
        if response.status_code != 200:
            return {
                "success": False,
                "data": None,
                "error": f"HTTP {response.status_code}"
            }

        
        user = response.json()

        
        required_fields = [
            "name",
            "email",
            "username"
        ]

        for field in required_fields:

            
            if field not in user:
                return {
                    "success": False,
                    "data": None,
                    "error": f"Missing Field: {field}"
                }

            if user[field] is None:
                return {
                    "success": False,
                    "data": None,
                    "error": f"Null Value: {field}"
                }

        return {
            "success": True,
            "data": user,
            "error": None
        }

    except requests.ConnectionError:

        return {
            "success": False,
            "data": None,
            "error": "ConnectionError"
        }

    except requests.Timeout:

        return {
            "success": False,
            "data": None,
            "error": "Timeout"
        }

    except Exception as e:

        return {
            "success": False,
            "data": None,
            "error": str(e)
        }



result = fetch_user(1)

if result["success"]:

    user = result["data"]

    print(f"Nama     : {user['name']}")
    print(f"Email    : {user['email']}")
    print(f"Username : {user['username']}")

else:

    print("Gagal mengambil data user")
    print(f"Error : {result['error']}")