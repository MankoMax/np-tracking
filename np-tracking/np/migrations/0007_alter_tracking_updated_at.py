# Generated by Django 4.1.3 on 2022-11-19 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('np', '0006_tracking_phone_recipient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracking',
            name='updated_at',
            field=models.DateTimeField(),
        ),
    ]
