from django.urls import path
from . import views

app_name = 'calculateResults'

urlpatterns = [
    path('', views.calculateResults , name="calculateResults"),
    path('displayResults/' , views.displayResults , name="displayResults"),
    path('calculateSubmit/' , views.calculateSubmit , name="calculateSubmit"),
    path('search/' , views.search , name="search"),
]