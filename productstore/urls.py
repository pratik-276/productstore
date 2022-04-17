from django.contrib import admin
from django.urls import path
from productuser import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage),
    path('login', views.login),
    path('signup', views.signup),
    path('productadd', views.addProduct),
    path('products', views.getproducts),
    path('add-product', views.addProduct)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)