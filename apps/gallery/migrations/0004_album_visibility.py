# Generated by Django 2.1 on 2019-11-22 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_auto_20191123_0254'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='visibility',
            field=models.BooleanField(default=True),
        ),
    ]
