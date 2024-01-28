# products/views.py
from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})
def your_view_name(request):
    print("View is being called")
    # Rest of your view logic
