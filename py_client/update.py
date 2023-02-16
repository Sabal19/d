from cgitb import html

import requests

data = {
    'title': 'lets do for update ',
    'price' : 20000
}


endpoint= "http://127.0.0.1:8000/1/update/"



get_response = requests.put(endpoint,json=data)
print(get_response.json()) 






