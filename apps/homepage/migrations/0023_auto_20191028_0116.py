# Generated by Django 2.1 on 2019-10-27 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0022_auto_20191028_0015'),
    ]

    operations = [
        migrations.AddField(
            model_name='recentprojects',
            name='order',
            field=models.IntegerField(default=1000),
        ),
        migrations.AddField(
            model_name='whatwedocards',
            name='order',
            field=models.IntegerField(default=1000),
        ),
        migrations.AddField(
            model_name='whychooseuscards',
            name='order',
            field=models.IntegerField(default=1000),
        ),
    ]