from django.db import models


class Department(models.Model):
    name = models.CharField(verbose_name='Adı', max_length=255)

    class Meta:
        verbose_name = 'Bölüm'
        verbose_name_plural = 'Bölümler'

    def __str__(self):
        return self.name


class Branch(models.Model):
    department = models.ForeignKey(Department, models.PROTECT, related_name='branchs')
    name = models.CharField(verbose_name='Adı', max_length=255)
    short_name = models.CharField(verbose_name='Kısaltılmışi', max_length=10)

    class Meta:
        verbose_name = 'Dal'
        verbose_name_plural = 'Dallar'

    def __str__(self):
        return self.short_name


class Klass(models.Model):
    name = models.CharField(verbose_name='Sınıf', max_length=10, help_text='Örneğin: "12"')
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='branches', verbose_name='Dal')

    class Meta:
        verbose_name = 'Sınıf'
        verbose_name_plural = 'Sınıflar'

    def __str__(self):
        return f'{self.name} {self.branch.short_name}'
