# Generated by Django 2.2.1 on 2019-06-05 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('branchs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Adı')),
                ('address', models.CharField(max_length=255, verbose_name='Adres')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=255, verbose_name='Telefon Numarası')),
                ('passive', models.BooleanField(default=False, verbose_name='Pasif')),
            ],
            options={
                'verbose_name': 'İşletme',
                'verbose_name_plural': 'İşletmeler',
            },
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Adı')),
            ],
            options={
                'verbose_name': 'Faaliyet Alanı',
                'verbose_name_plural': 'Faaliyet Alanları',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='StudentQualification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(choices=[('Yaz', 'Yaz'), ('Kış', 'Kış')], max_length=3, verbose_name='Grup')),
                ('period', models.CharField(blank=True, choices=[('1', 'P.tesi, Salı, Çarşamba'), ('2', 'Çarşamba, Perşembe, Cuma')], max_length=1, null=True, verbose_name='Haftalık Periyot')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Başlama Tarihi')),
                ('finish_date', models.DateField(blank=True, null=True, verbose_name='Bitiş Tarihi')),
                ('piece', models.PositiveSmallIntegerField(verbose_name='Öğrenci Sayısı')),
                ('qualifications', models.TextField(blank=True, null=True, verbose_name='Nitelikler')),
                ('branch', models.ManyToManyField(to='branchs.Branch', verbose_name='Dal')),
            ],
            options={
                'verbose_name': 'Stajyer İsteği',
                'verbose_name_plural': 'Stajyer İstekleri',
            },
        ),
    ]