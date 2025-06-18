from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=30)
    desc = models.TextField("describtion") 
    created = models.DateTimeField("creation_date", auto_now_add=True)
    is_deleted = models.BooleanField() # add default
    # creator_user
    image_url = models.CharField(max_length=100, null = True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comments")
    desc = models.TextField("describtion")
    created = models.DateTimeField("creation_date", auto_now_add=True)
    is_deleted = models.BooleanField()
    #creator_user

    def __str__(self):
        return f"[{self.product}] {self.desc[:30]}{"" if len(self.desc)<30 else "..."}"

class Category(models.Model):
    name = models.CharField(max_length=30)
    products = models.ManyToManyField(Product, related_name="categories")
    is_deleted = models.BooleanField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

