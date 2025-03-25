import requests

endpoint = "http://localhost:8000/api/products/1/update/"

data = {
    "title": "Updated title",
    "content": "Updated content",
    "price": 199,
}

get_response = requests.put(endpoint , json=data)  # HTTP Request

print(get_response.json())
