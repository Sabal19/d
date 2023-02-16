

import requests




endpoint= "http://127.0.0.1:8000/13456765434566123234567"



get_response = requests.get(endpoint)
print(get_response.json()) 






