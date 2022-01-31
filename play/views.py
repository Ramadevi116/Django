from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'home.html')
def products(request):
    return render(request,'product.html')
def customer(request):
    return render(request,'customer.html')