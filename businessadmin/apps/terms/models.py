from django.db import models


class Term(models.CharField):
    name = models.CharField(verbose_name='Adı', max_length=255, help_text='Örnek: "2019 - 2020" ')
    archive = models.BooleanField(verbose_name='Arşivlensin mi?', default=False)

    class Meta:
        verbose_name = 'Dönem'
        verbose_name_plural = 'Dönemler'

    def __str__(self):
        return self.name

    def set_as_archive(self):
        self.active = True
