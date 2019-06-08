from django.db import models
from django.shortcuts import reverse


class Sector(models.Model):
    name = models.CharField(verbose_name='Adı', max_length=255)

    class Meta:
        verbose_name = 'Faaliyet Alanı'
        verbose_name_plural = 'Faaliyet Alanları'
        ordering = ('name',)


class Business(models.Model):
    name = models.CharField(verbose_name='Adı', max_length=255)
    address = models.CharField(verbose_name='Adres', max_length=255)
    email = models.EmailField()
    phone = models.CharField(verbose_name='Telefon Numarası', max_length=255)
    passive = models.BooleanField(verbose_name='Pasif', default=False)
    manager = models.OneToOneField('members.Member', on_delete=models.PROTECT, related_name='business',
                                   verbose_name='Yetkili')

    class Meta:
        verbose_name = 'İşletme'
        verbose_name_plural = 'İşletmeler'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('business:detail', kwargs={'pk': self.pk})


class StudentQualification(models.Model):
    period_choices = (('1', 'P.tesi, Salı, Çarşamba'), ('2', 'Çarşamba, Perşembe, Cuma'))
    group = models.CharField(verbose_name='Grup', choices=(('Yaz', 'Yaz'), ('Kış', 'Kış')), max_length=3)
    period = models.CharField(verbose_name='Haftalık Periyot', choices=period_choices, max_length=1, null=True,
                              blank=True)
    start_date = models.DateField(verbose_name='Başlama Tarihi', null=True, blank=True)
    finish_date = models.DateField(verbose_name='Bitiş Tarihi', null=True, blank=True)
    piece = models.PositiveSmallIntegerField(verbose_name='Öğrenci Sayısı')
    branch = models.ManyToManyField('branchs.Branch', verbose_name='Dal')
    qualifications = models.TextField(verbose_name='Nitelikler', null=True, blank=True)
    business = models.ForeignKey('businesses.Business', verbose_name='İşletme', on_delete=models.CASCADE,
                                 related_name='qualificaions')

    class Meta:
        verbose_name = 'Stajyer İsteği'
        verbose_name_plural = 'Stajyer İstekleri'

    def __str__(self):
        return f'{self.branch} - {self.group} - {self.period}'
