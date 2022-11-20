from django.urls import path
from .views import HomeView, add_ttn


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add_ttn/', add_ttn, name='add_ttn'),
]