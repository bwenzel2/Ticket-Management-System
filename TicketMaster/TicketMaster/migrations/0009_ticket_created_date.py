# Generated by Django 2.0.2 on 2018-02-24 17:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('TicketMaster', '0008_auto_20180224_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
