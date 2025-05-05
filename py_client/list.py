import requests
from getpass import getpass

auth_endpoint = "http://127.0.0.1:8000/api/auth/"
username = input("Enter your username:\n")
password = getpass("Enter your password:\n")

auth_response = requests.post(
    auth_endpoint,
    json={
        "username": "youssef",
        "password": 1234
        },
)  # HTTP Request
print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()["token"]
    headers = {"Authorization": f"bearer {token}"}
    end_point = "http://127.0.0.1:8000/api/products/list/"
    ger_responce = requests.get(end_point, headers=headers)
    print(ger_responce.json())