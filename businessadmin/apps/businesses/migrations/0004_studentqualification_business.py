# Generated by Django 2.2.1 on 2019-06-07 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('businesses', '0003_auto_20190607_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentqualification',
            name='business',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='qualificaions', to='businesses.Business', verbose_name='İşletme'),
            preserve_default=False,
        ),
    ]
