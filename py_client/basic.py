from cgitb import html
from urllib.request import Request
from webbrowser import get
import requests


# endpoint = "htttps://httpbin.org/status/200/ "
endpoint= "https://httpbin.org/anything"
endpoint= "http://127.0.0.1:8000/"



get_response = requests.post(endpoint,params={"abc":"123"},json={'title':"Hello world "}) # library API || is http request
print(get_response.json()) 
# print(get_response.text)
# print(get_response.headers)


# HTTP Request -> html
# REST API Request -> JSON(XML)



