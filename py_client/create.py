import requests

endpoint = "http://localhost:8000/api/products/create/" 

data = {
    "title" : "Yousssef",
    "price" : 99.99
} 

get_response = requests.post(endpoint , json=data) # HTTP Request

print(get_response.json())
