# Generated by Django 4.1.3 on 2022-11-17 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('np', '0002_alter_tracking_delivered_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tracking',
            name='delivered_date',
        ),
    ]
