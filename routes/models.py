from django.db import models
from .data_reader import routes_gen

# Create your models here.

class Price(models.Model):
    number = models.CharField(max_length=17)
    price = models.CharField(max_length=6)


class CarrierList(models.Model):
    data = models.FileField()

    def save(self, *args, **kwargs):
        super(CarrierList, self).save(*args, **kwargs)
        filename = self.data.url
        prices = []
        for (number, price) in routes_gen(filename):
            number = str(number)
            price = str(price)
            
            obj = Price(number=number, price=price)
            prices.append(obj)
        
        Price.objects.bulk_create(prices)

def get_price(number):
    print("getting price")
    prefix = number
    while prefix != "":
        print("checking prefix:", prefix)
        try:
            price = Price.objects.get(number=prefix).price
            print("found price:", price)
            return str(price)
        except Price.DoesNotExist:
            prefix = prefix[:-1]
        except Price.MultipleObjectsReturned:
            routes = Price.objects.filter(number=prefix)
            prices = [route.price for route in routes]

            return min(prices)
    
    print("could not find an entry :(")
    return "No route found."
