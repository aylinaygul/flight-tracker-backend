# Generated by Django 5.1.7 on 2025-03-22 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight_tracker_app', '0002_remove_flight_flight_id_flight_model_flight_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='model',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
