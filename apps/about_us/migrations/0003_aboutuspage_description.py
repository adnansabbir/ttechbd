# Generated by Django 2.1 on 2019-08-29 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_us', '0002_auto_20190828_0147'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutuspage',
            name='description',
            field=models.TextField(max_length=2000, null=True),
        ),
    ]
