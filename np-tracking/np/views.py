from django.shortcuts import redirect, render
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
            ttn = ttn.replace('\t', '').split(',')
        result = get_ttn(ttn, phone)
        if result != 'Wrong ttn':
            for i in result:
                #TODO при вводе списка, добавляет несколько уже существующих элементов
                if not Tracking.objects.all().filter(ttn=ttn):
                    Tracking.objects.create(
                    ttn=i['ttn'],
                    status=i['status'],
                    sent_date=i['sent_date'],
                    schedule_date=i['schedule_date'],
                    recipient_city=i['recipient_city'],
                    recipient_name=i['recipient_name'],
                    afterpayment_cost=i['afterpayment_cost'],
                    phone_sender=i['phone_sender'])
        return redirect('home')
    return redirect('home')


def delete_ttn(request, id):
    ttn = Tracking.objects.get(id=id)
    ttn.delete()
    return redirect('home')


def delete_all_ttn(request):
    Tracking.objects.all().delete()
    return redirect('home')


def update_ttn(request, id):
    ttn = Tracking.objects.get(id=id)
    result = get_ttn(ttn.ttn, ttn.phone_sender)
    for i in result:
        Tracking.objects.filter(id=ttn.pk).update(
            ttn=i['ttn'],
            status=i['status'],
            sent_date=i['sent_date'],
            schedule_date=i['schedule_date'],
            recipient_city=i['recipient_city'],
            recipient_name=i['recipient_name'],
            afterpayment_cost=i['afterpayment_cost'],
            phone_recipient=i['phone_recipient'])
    return redirect('home')


def update_all_ttn(request):
    ttns = list(Tracking.objects.all())
    for ttn in ttns:
        result = get_ttn(ttn.ttn, ttn.phone_sender)
        for i in result:
            Tracking.objects.select_for_update().filter(id=ttn.pk).update(
            ttn=i['ttn'],
            status=i['status'],
            sent_date=i['sent_date'],
            schedule_date=i['schedule_date'],
            recipient_city=i['recipient_city'],
            recipient_name=i['recipient_name'],
            afterpayment_cost=i['afterpayment_cost'],
            phone_recipient=i['phone_recipient'])
    return redirect('home')