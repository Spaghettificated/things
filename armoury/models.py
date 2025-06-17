from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=30)
    describtion = models.TextField()
    creation_date = models.DateField(auto_now=False, auto_now_add=False)
    is_deleted = models.BooleanField()
    # creator_user
    image_url = models.CharField(max_length=100, )


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.TextField()
    creation_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    is_deleted = models.BooleanField()
    #creator_user

class Category(models.Model):
    name = models.CharField(max_length=30)
    products = models.ManyToManyField(Product)
    is_deleted = models.BooleanField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE)

