# Generated by Django 4.1.3 on 2022-11-17 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('np', '0003_remove_tracking_delivered_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='tracking',
            name='phone_sender',
            field=models.CharField(default=380960042412, max_length=20),
            preserve_default=False,
        ),
    ]