# Generated by Django 5.0.6 on 2024-07-01 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0006_alter_reservatie_res_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservatie',
            name='res_time',
        ),
        migrations.AlterField(
            model_name='reservatie',
            name='res_date',
            field=models.DateTimeField(verbose_name='Reservation date'),
        ),
    ]
