# Generated by Django 4.2.8 on 2023-12-20 11:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 20, 11, 36, 19, 995826, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='date_last_ban',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 20, 11, 36, 19, 995867, tzinfo=datetime.timezone.utc)),
        ),
    ]
