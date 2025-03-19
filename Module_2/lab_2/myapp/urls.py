from django.urls import path   # Import path
from . import views            # Import views from views.py

urlpatterns = [
    path('drinks/<str:drink_name>', views.drinks, name="drink_name"),
]