from django.shortcuts import render
from django.http import JsonResponse
from pandas.compat import StringIO
from django.views.decorators.csrf import csrf_exempt
import json
from .models import ProductUser


def authpage(request):
    return render(request, 'login.html')


@csrf_exempt
def signup(req):
    email = req.POST.get('email')
    password = req.POST.get('password')

    try:
        user = ProductUser(email=email, password=password)
        user.save()
        return JsonResponse({
            "message": "User creation success"
        })
    except:
        return JsonResponse({
            "message": "User creation failed"
        })


@csrf_exempt
def login(req):
    email = req.POST.get('email')
    password = req.POST.get('password')

    try:
        user = ProductUser.objects.get(email=email)
        print(user.password)
        return render(req, 'login.html')
    except:
        print("User does not exist")
        return JsonResponse({
            "message": "User does not exist"
        })
