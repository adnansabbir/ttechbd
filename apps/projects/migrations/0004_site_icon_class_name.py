# Generated by Django 2.1 on 2019-08-27 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20190819_0018'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='icon_class_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
