# Generated by Django 2.1 on 2019-10-03 19:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0018_sliderimages_show_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sliderimages',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
