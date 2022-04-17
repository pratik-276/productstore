from django.shortcuts import render
from django.http import JsonResponse
from pandas.compat import StringIO
from django.views.decorators.csrf import csrf_exempt
import json
from .models import ProductUser, Product
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect


def homePage(request):
    return render(request, 'login.html')


@csrf_exempt
def signup(req):
    if req.method == "POST":
        email = req.POST.get('email')
        password = req.POST.get('password')
        address = req.POST.get('address')
        mobile_number = req.POST.get('mobile_number')
        first_name = req.POST.get('first_name')
        last_name = req.POST.get('last_name')

        try:
            user = ProductUser.objects.get(email=email)
            return render(req, 'signup.html', {
                "message": "Email already exists. Please login"
            })
        except:
            pass

        try:
            user = ProductUser(email=email, password=password, first_name=first_name, last_name=last_name,
                                address=address, mobile_number=mobile_number)
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
            return redirect('/products')
        except:
            return render(req, 'login.html', {'message': "User does not exist"})
    elif req.method == "GET":
        return render(req, 'login.html')


@csrf_exempt
def addProduct(req):
    if req.method == "POST":
        name = req.POST.get('name')
        image_file = req.FILES['file']
        description = req.POST.get('description')

        # fss = FileSystemStorage()
        # file = fss.save(image_file.name, image_file)
        # file_url = fss.url(file)

        try:
            product = Product(name=name, link=image_file, description=description)
            product.save()
            return redirect('/products')
        except:
            return JsonResponse({
                "message": "Product creation failed"
            })
    else:
        return render(req, 'addproduct.html')


@csrf_exempt
def getproducts(req):
    if req.method == "GET":
        products = Product.objects.all()
        fetched_products = []
        for product in products:
            temp = {
                "name": product.name,
                "link": product.link.name,
                "description": product.description
            }
            fetched_products.append(temp)
        return render(req, 'products.html', {
            "products": fetched_products
        })
