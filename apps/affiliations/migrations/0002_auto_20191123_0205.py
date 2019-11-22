# Generated by Django 2.1 on 2019-11-22 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('affiliations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AffiliateProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background_image', models.ImageField(blank=True, null=True, upload_to='AffiliateProjects/MainImages/BackgroundImages')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('image', models.ImageField(upload_to='AffiliateProjects/MainImages/')),
            ],
        ),
        migrations.CreateModel(
            name='AffiliateProjectImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='AffiliateProjects/ExtraImages/')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='affiliations.AffiliateProject')),
            ],
        ),
        migrations.CreateModel(
            name='AffiliateProjectType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='affiliationpage',
            name='background_image',
            field=models.ImageField(upload_to='Site/AffiliationsPage/'),
        ),
        migrations.AlterField(
            model_name='affiliationpage',
            name='title',
            field=models.CharField(default='Affiliations', max_length=20),
        ),
        migrations.AddField(
            model_name='affiliateproject',
            name='type',
            field=models.ManyToManyField(to='affiliations.AffiliateProjectType'),
        ),
    ]