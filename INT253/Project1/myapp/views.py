from django.http import HttpResponse
import requests
from django.http import JsonResponse

def hello_world(request):
    return HttpResponse("Hello, World!")

def even_odd(request):
        a=2024
        if(a%2==0):
            return HttpResponse("No. is even")
        else:
            return HttpResponse("No. is odd")


def prime(request):
    n = 10
    if n <= 1:
        return HttpResponse("false")
    
    for i in range(2, n):
        if n % i == 0:
            return HttpResponse("false")
    
    return HttpResponse("True")


def get_api_data(request,id):
    url = f'https://jsonplaceholder.typicode.com/posts/{id}' 
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data)

    else:
        return JsonResponse({"error": "Failed to fetch data"}, status = 500)



def json_lpu(request):
    data = {
        "name": "Mahesh", 
        "age": "22",
    }
    return JsonResponse(data)



# def json_simpleview2(request,data):
#     d = {
#         "name": ""
#     }

# Create your views here.

def greet(request, name):
    return HttpResponse(f"Hello, {name}!")



def report(request, date):
    return HttpResponse(f"Report for date: {date}")