from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 
from cars.views import NewCarCreateView, CarsListView, CarDetailView, CarUpdateView, CarDeleteView, AboutUs

app_name = 'cars'

urlpatterns = [
    path('', CarsListView.as_view(), name='home'),
    path('cars/', CarsListView.as_view(), name='cars_list'),
    path('novo_carro/', NewCarCreateView.as_view(), name='new_car_view'),
    path('car/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('car/<int:pk>/update', CarUpdateView.as_view(), name='car_update'),
    path('car/<int:pk>/delete', CarDeleteView.as_view(), name='car_delete'),
    path('about/', AboutUs.as_view(), name='about_us')
]
