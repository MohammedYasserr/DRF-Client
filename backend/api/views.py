from django.http import JsonResponse
import json

def api_home(request , *args, **kwargs):
    body = request.body 
    data ={}
    print(request.GET) #It will return url query parameter
    print(request.POST)
    try:
        data = json.loads(body) #This takes in String of json data --> returns a python dictionary
    except:
        pass
    
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)
