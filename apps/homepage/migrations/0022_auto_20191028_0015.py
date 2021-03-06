# Generated by Django 2.1 on 2019-10-27 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0021_whatwedocards_icon_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Icons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('icon_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='homepage.IconHTMLTag')),
            ],
        ),
        migrations.RemoveField(
            model_name='whatwedocards',
            name='icon_name',
        ),
        migrations.AlterField(
            model_name='whatwedocards',
            name='icon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='homepage.Icons'),
        ),
        migrations.AlterField(
            model_name='whychooseuscards',
            name='icon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='homepage.Icons'),
        ),
        migrations.DeleteModel(
            name='FlatIconsClassName',
        ),
    ]
