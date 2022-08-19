from pydoc import describe
from django.db import models

class Product(models.Model):
    name = models.CharField("Name", max_length=240)
    description = models.TextField("Description")
    price = models.FloatField("Price")

    def __str__(self):
        return self.name