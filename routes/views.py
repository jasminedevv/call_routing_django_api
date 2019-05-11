from django.shortcuts import render
from .models import Price, get_price

from django.http import HttpResponse
from django.http import JsonResponse


def return_price(request, number):
    print("\nFetching price\n")
    # number = request.GET["number"]
    price = get_price(number)
    print("for number:", number)
    
    return JsonResponse({'price':price})