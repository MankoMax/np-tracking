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
                try:
                    tracking = Tracking.objects.filter(ttn=i['ttn']).first()
                    tracking.status = i['status']
                    tracking.sent_date = i['sent_date']
                    tracking.schedule_date = i['schedule_date']
                    tracking.recipient_city = i['recipient_city']
                    tracking.recipient_name = i['recipient_name']
                    tracking.afterpayment_cost = i['afterpayment_cost']
                    tracking.save()
                except Tracking.DoesNotExist:
                    Tracking.objects.create(
                        ttn=i['ttn'],
                        status=i['status'],
                        sent_date=i['sent_date'],
                        schedule_date=i['schedule_date'],
                        recipient_city=i['recipient_city'],
                        recipient_name=i['recipient_name'],
                        afterpayment_cost=i['afterpayment_cost']
                    )
        return redirect('home')
    return redirect('home')