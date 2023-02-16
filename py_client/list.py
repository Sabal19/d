
import requests
from getpass import getpass


auth_endpoint= "http://127.0.0.1:8000/api/auth/"

username = input('Your Username:')
password = getpass('Your Password')


auth_response = requests.post(auth_endpoint,json={'username':username,'password':password})

print(auth_response.json())

if auth_response.status_code==200:
    token = auth_response.json()['token']
    headers ={
        # 'Authorization': f'Token {token}'
        'Authorization': f'Bearer {token}'  # This Bearer can be written by overwriting keyword in TokenAuthentication as done in api/authentication.py
    }
    endpoint= "http://127.0.0.1:8000/"
    get_response = requests.get(endpoint,headers=headers)
    # print(get_response.json())

    #for pagination
    data = get_response.json()
    results = data['results']
    next_url = data['next']
    print(results)
    print('next url:',next_url)















# endpoint= "http://127.0.0.1:8000/"

# data={
#     'title':"This is the title assigned to the create api view"
# }


# get_response = requests.get(endpoint,json=data)
# print(get_response.json()) 

