# Generated by Django 2.1 on 2019-11-22 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Albums',
            new_name='Album',
        ),
        migrations.RenameModel(
            old_name='Images',
            new_name='Image',
        ),
    ]

    atomic = False
