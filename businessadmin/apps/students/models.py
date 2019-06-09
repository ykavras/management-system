from django.db import models
from django.urls import reverse_lazy


class Student(models.Model):
    member = models.OneToOneField('members.Member', on_delete=models.PROTECT,
                                  related_name='student', verbose_name='Kullanıcı')
    number = models.PositiveIntegerField(verbose_name='Okul Numarası')
    term = models.ForeignKey('terms.Term', verbose_name='Dönem', on_delete=models.CASCADE, related_name='students')
    klass = models.ForeignKey('branchs.Klass', on_delete=models.CASCADE, related_name='students', verbose_name='Sınıf')

    class Meta:
        verbose_name = 'Öğrenci'
        verbose_name_plural = 'Öğrenciler'

    def __str__(self):
        return f'{self.member.user.get_full_name()} - {self.member.user.username}'

    def get_absolute_url(self):
        return reverse_lazy('student:detail', kwargs={'pk': self.pk})
