# Generated by Django 2.2 on 2019-07-01 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190629_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='wedding_rehearsal',
            field=models.BooleanField(default=False),
        ),
    ]
