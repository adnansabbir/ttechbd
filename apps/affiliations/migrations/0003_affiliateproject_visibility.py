# Generated by Django 2.1 on 2019-11-22 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('affiliations', '0002_auto_20191123_0205'),
    ]

    operations = [
        migrations.AddField(
            model_name='affiliateproject',
            name='visibility',
            field=models.BooleanField(default=True),
        ),
    ]
