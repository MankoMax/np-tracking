from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Tracking
from .utils import get_ttn

class HomeView(TemplateView):
    template_name = 'np/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        trackings = Tracking.objects.all()
        context['trackings'] = trackings
        return context


def add_ttn(request):
    if request.method == 'POST':
        ttn = request.POST.get('ttn')
        phone = request.POST.get('phone')
        if "," in ttn:
            ttn = ttn.split(',')
        result = get_ttn(ttn, phone)
        if result != 'Wrong ttn':
            for i in result:
                Tracking.objects.create(**i)
        return redirect('home')
    return redirect('home')