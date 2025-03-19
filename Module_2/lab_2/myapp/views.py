from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse  # Import HttpResponse

def drinks(request, drink_name):
    # Step 3: Create a dictionary of drinks
    drink = {
        'mocha': 'type of coffee',
        'tea': 'type of beverage',
        'lemonade': 'type of refreshment'
    }

    # Step 4: Assign the value from the dictionary
    choice_of_drink = drink.get(drink_name, "Sorry, this drink is not available")

    # Step 5: Return the response
    return HttpResponse(f"<h2>{drink_name}</h2>{choice_of_drink}")
