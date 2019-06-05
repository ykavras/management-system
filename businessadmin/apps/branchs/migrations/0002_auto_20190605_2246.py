# Generated by Django 2.2.1 on 2019-06-05 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('branchs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='branchs', to='branchs.Department', verbose_name='Bölüm'),
        ),
        migrations.AlterField(
            model_name='branch',
            name='short_name',
            field=models.CharField(max_length=10, verbose_name='Kısaltılmışı'),
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Bölüm Adı'),
        ),
    ]
