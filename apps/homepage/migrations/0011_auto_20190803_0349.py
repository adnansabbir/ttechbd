# Generated by Django 2.2.4 on 2019-08-02 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0010_auto_20190803_0338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='whatwedocards',
            name='what_we_do_section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='card', to='homepage.WhatWeDoSection'),
        ),
    ]
