# Generated by Django 5.0.6 on 2024-07-01 16:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0007_remove_reservatie_res_time_alter_reservatie_res_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservatie',
            name='res_time',
            field=models.TimeField(default=datetime.time(12, 0)),
            preserve_default=False,
        ),
    ]
