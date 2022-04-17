from django.db import models


class ProductUser(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    address = models.TextField()
    mobile_number = models.CharField(max_length=13)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email