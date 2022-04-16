from django.shortcuts import render
# from django.http import JsonResponse
# from pandas.compat import StringIO
# from django.views.decorators.csrf import csrf_exempt
# import json


def login(request):
    return render(request, 'login.html')
