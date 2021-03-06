# Generated by Django 2.2.4 on 2019-08-02 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0014_recentprojects'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_1_title', models.CharField(max_length=25)),
                ('menu_2_title', models.CharField(max_length=25)),
                ('menu_3_title', models.CharField(max_length=25)),
                ('menu_1_links', models.ManyToManyField(related_name='menu_1_links', to='homepage.FooterLink')),
                ('menu_2_links', models.ManyToManyField(related_name='menu_2_links', to='homepage.FooterLink')),
                ('menu_3_links', models.ManyToManyField(related_name='menu_3_links', to='homepage.FooterLink')),
            ],
        ),
    ]
