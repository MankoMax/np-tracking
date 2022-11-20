from django.contrib import admin
from django.urls import path
from .views import HomeView, add_ttn, delete_ttn, delete_all_ttn, update_ttn, update_all_ttn


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add_ttn/', add_ttn, name='add_ttn'),
    path('delete_ttn/<int:id>', delete_ttn, name='delete_ttn'),
    path('delete_all_ttn/', delete_all_ttn, name='delete_all_ttn'),
    path('update_ttn/<int:id>', update_ttn, name='update_ttn'),
    path('update_all_ttn/', update_all_ttn, name='update_all_ttn'),
]