# CS 1.3 Call Routing Project
## By Jasmine and Dacio

This is the API for scenario 4 of the call routing project. It is simply a Django app with a hook that adds route costs to a SQL database when a carrier list file is uploaded.

The program matches the most specific prefix and returns the cheapest route if multiple are found.

It is functionally very similar to our scenario 2 solution.

Example:
https://call-api-jasmine-dacio-django.herokuapp.com/get-price/+4990569325

It contains costs found in route-costs-106000.txt, route-costs-35000.txt, and as much of route-costs-10000000.txt as Heroku's free-tier Postrges database could eat.

### How to grade
The important logic is found in routes/models.py. Everything else is just web stuff.
