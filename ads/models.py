from django.db import models


class Adv(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.CharField(max_length=1000)
    address = models.CharField(max_length=300)
    is_published = models.BooleanField(default=False)


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
