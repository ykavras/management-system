# Generated by Django 2.2.1 on 2019-06-08 02:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('businesses', '0005_business_coordinator'),
        ('students', '0003_auto_20190607_2323'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='business',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='students', to='businesses.Business', verbose_name='İşletme'),
        ),
    ]
