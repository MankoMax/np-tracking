from django.db import models



class Tracking(models.Model):
    
    ttn = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    sent_date = models.DateField()
    schedule_date = models.DateField()
    recipient_city = models.CharField(max_length=255)
    recipient_name = models.CharField(max_length=255)
    afterpayment_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    phone_sender = models.CharField(max_length=20)
    phone_recipient = models.CharField(max_length=20)


    def __str__(self):
        return self.ttn
