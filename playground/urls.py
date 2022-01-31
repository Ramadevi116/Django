from django.urls import path
from . import views
# URL conf
urlpatterns = [
    path('hello/',views.say_hello)
]