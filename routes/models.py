from django.db import models
from .data_reader import routes_gen

# Create your models here.

class Price(models.Model):
    number = models.IntegerField()
    price = models.FloatField()


class CarrierList(models.Model):
    data = models.FileField()

    def save(self, *args, **kwargs):
        super(CarrierList, self).save(*args, **kwargs)
        filename = self.data.url
        # Do anything you'd like with the data in filename
        for (number, price) in routes_gen(filename):
            obj = Price(number=number, price=price)
            obj.save() 

def get_price(number):
    print("getting price")
    prefix = number
    while prefix != "":
        print("checking prefix:", prefix)
        try:
            price = Price.objects.get(number=number).price
            print("found price:", price)
            return str(price)
        except Price.DoesNotExist:
            print("could not find an entry :(")
            return 0
