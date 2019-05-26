from django.db import models


class Department(models.Model):
    name = models.CharField(verbose_name='Adı', max_length=255)

    class Meta:
        verbose_name = 'Bölüm'
        verbose_name_plural = 'Bölümler'


class Branch(models.Model):
    department = models.ForeignKey(Department, models.PROTECT, related_name='branchs')
    name = models.CharField(verbose_name='Adı', max_length=255)

    class Meta:
        verbose_name = 'Dal'
        verbose_name_plural = 'Dallar'
