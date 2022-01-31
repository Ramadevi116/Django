from django.urls import path
from . import views
# URL conf
urlpatterns = [
    
    path('',views.home),
    path('products/',views.products),
    path('customer/',views.customer),
]