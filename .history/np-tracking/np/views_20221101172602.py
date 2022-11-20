from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Tracking

class HomeView(TemplateView):
    template_name = 'np/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        trackings = Tracking.objects.all()
        return context