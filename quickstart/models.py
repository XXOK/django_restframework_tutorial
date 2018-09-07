from django.db import models


class Person(models.Model):

    name = models.CharField(max_length=10)
    age = models.IntegerField()
    region = models.CharField(max_length=30)