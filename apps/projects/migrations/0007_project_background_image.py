# Generated by Django 2.1 on 2019-10-04 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_projectpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='background_image',
            field=models.ImageField(blank=True, null=True, upload_to='Projects/MainImages/BackgroundImages'),
        ),
    ]
