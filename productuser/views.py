from django.shortcuts import render
from django.http import JsonResponse
from pandas.compat import StringIO
from django.views.decorators.csrf import csrf_exempt
import json
from .models import ProductUser, Product, Own, Transaction
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
            return redirect('/login')
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
            return redirect(f'/products?userid={user.id}')
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
        userid = req.GET.get('userid')
        products = Product.objects.all()
        fetched_products = []
        for product in products:
            own_count = 0
            try:
                own = Own.objects.get(userid=int(userid), productid=product.id)
                own_count = own.count
            except:
                pass
            temp = {
                "id": product.id,
                "name": product.name,
                "link": product.link.name,
                "description": product.description,
                "count": own_count
            }
            fetched_products.append(temp)
        return render(req, 'products.html', {
            "products": fetched_products
        })


@csrf_exempt
def addtransaction(req):
    if req.method == "GET":
        userid = req.GET.get('uid')
        productid = req.GET.get('pid')
        status = req.GET.get('status')

        try:
            transaction = Transaction(userid=int(userid), productid=int(productid), status=status)
            transaction.save()

            try:
                own = Own.objects.get(userid=int(userid), productid=int(productid))
                if status == "buy":
                    own.count += 1
                else:
                    if own.count > 0:
                        own.count -= 1
                own.save()
            except:
                try:
                    own = Own(userid=int(userid), productid=int(productid), count=1)
                    own.save()
                except:
                    print("Saving own failed")
        except:
            print("Saving Transaction Failed")

        return redirect(f'/products?userid={userid}')