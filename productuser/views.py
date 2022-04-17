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
    if req.method == "POST":
        email = req.POST.get('email')
        password = req.POST.get('password')

        try:
            user = ProductUser.objects.get(email=email)
            return render(req, 'signup.html', {
                "message": "Email already exists. Please login"
            })
        except:
            pass

        try:
            user = ProductUser(email=email, password=password)
            user.save()
            return JsonResponse({
                "message": "User creation success"
            })
        except:
            return render(req, 'signup.html', {'message': "User creation failed"})
    elif req.method == "GET":
        return render(req, 'signup.html')


@csrf_exempt
def login(req):
    if req.method == "POST":
        email = req.POST.get('email')
        password = req.POST.get('password')

        try:
            user = ProductUser.objects.get(email=email)
            if user.password != password:
                return render(req, 'login.html', {'message': 'Password incorrect'})
            return JsonResponse({
                "message": "Login Success"
            })
        except:
            return render(req, 'login.html', {'message': "User does not exist"})
    elif req.method == "GET":
        return render(req, 'login.html')
