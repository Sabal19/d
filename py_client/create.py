
import requests


# session -> post data ----have first session and post data 

endpoint= "http://127.0.0.1:8000/"

#lets try by directly passing the token
headers = {'Authorization': 'Bearer f6993e2195fdde534c4abde41a374ecb855f2850'}  #This token was generated when logged into /auth/ as shown in list.py
data={
    'title':"This is the title assigned to the create api view"
}

get_response = requests.post(endpoint,json=data,headers=headers)
print(get_response.json()) 

