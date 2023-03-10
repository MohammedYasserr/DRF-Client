from django.http import JsonResponse
import json

def api_home(request , *args, **kwargs):
    body = request.body 
    data ={}
    try:
        data = json.loads(body) #This takes in String of json data --> returns a python dictionary
    except:
        pass
    print(data.keys())
    #print(body) )
    return JsonResponse(data)
