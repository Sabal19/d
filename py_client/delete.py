import requests

product_id = input(("Enter the product ID you want to use?\n"))

try:
    product_id=int(product_id)

except:
    product_id = None
    print(f'{product_id} is not a valid product id to send')



if product_id:
    endpoint=f"http://127.0.0.1:8000/{product_id}/delete/"



get_response = requests.delete(endpoint)
print(get_response.status_code,get_response==204)  