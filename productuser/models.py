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


class Product(models.Model):
    name = models.CharField(max_length=255)
    link = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Own(models.Model):
    userid = models.IntegerField()
    productid = models.IntegerField()
    count = models.IntegerField()

    def __str__(self):
        return self.userid


class Transaction(models.Model):
    userid = models.IntegerField()
    productid = models.IntegerField()
    status = models.CharField(max_length=15)

    def __str__(self):
        return self.userid
