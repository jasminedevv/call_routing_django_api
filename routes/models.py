from django.db import models
from .data_reader import routes_gen

# Create your models here.

class Price(models.Model):
    """Route and its cost"""
    number = models.CharField(max_length=17)
    price = models.CharField(max_length=6)


class CarrierList(models.Model):
    """Text file with carrier route prices"""
    data = models.FileField()

    def save(self, *args, **kwargs):
        """Adds carrier route prices to db whenever a new carrier list is uploaded"""
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
    """Fetches the most specific matching route cost of a number and returns the cheapest option if multiple are found"""
    print("getting price")
    prefix = number
    while prefix != "":
        print("checking prefix:", prefix)
        try:
            price = Price.objects.get(number=prefix).price
            return str(price)
        except Price.DoesNotExist:
            prefix = prefix[:-1]
        except Price.MultipleObjectsReturned:
            routes = Price.objects.filter(number=prefix)
            prices = [route.price for route in routes]

            return min(prices)
    
    return "0"
