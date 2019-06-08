from django.db import models
from django.urls import reverse_lazy


class Teacher(models.Model):
    member = models.OneToOneField('members.Member', verbose_name='Kullanıcı', on_delete=models.PROTECT,
                                  related_name='teacher')
    phone = models.CharField(verbose_name='Tel', max_length=20)

    class Meta:
        verbose_name = 'Öğretmen'
        verbose_name_plural = 'Öğretmenler'

    def is_chief(self):
        return self.member.type == 'Chief'

    def __str__(self):
        return self.member.user.get_full_name()

    def get_absolute_url(self):
        return reverse_lazy('teacher:detail', kwargs={'pk': self.pk})
