# Generated by Django 2.2.4 on 2019-08-02 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_company_color1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='phone',
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
