from django.shortcuts import render
from django.http import JsonResponse
import json
# Create your views here.
def api_home(request,*args,**kwargs):
    body = request.body
    print(request.GET) #url query parameters
    data ={}
    try:
        data=json.loads(body)  # converts strings of json data to dictionary

    except:
        pass
    # print(data)
    data['params']= dict(request.GET)
    data['headers']=dict(request.headers)
    data['content_type']=request.content_type 
    print(data['headers'])
    print(data['content_type'])
    return JsonResponse(data)

