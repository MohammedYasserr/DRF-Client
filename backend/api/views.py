from django.http import JsonResponse

def api_home(request , *args, **kwargs):
    return JsonResponse({"messgae" : "Hello, this is Django api response"})
