import requests


produt_id = input(f"Enter the product id that you want to delete: ")

try:
    produt_id = int(produt_id)
except:
    produt_id = None
    print(f"{produt_id} this id is not vaid.")

endpoint = f"http://localhost:8000/api/products/{produt_id}/delete/"
get_response = requests.delete(endpoint)  # HTTP Request

print(get_response.status_code, get_response.status_code==204)  # Response
