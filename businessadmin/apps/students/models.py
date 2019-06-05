from django.db import models


class Student(models.Model):
    term = models.ForeignKey('terms.Term', verbose_name='Dönem', on_delete=models.CASCADE, related_name='students')
    number = models.PositiveIntegerField(verbose_name='Okul Numarası')
    klass = models.ForeignKey('branchs.Klass', on_delete=models.CASCADE, related_name='students', verbose_name='Sınıf')

    class Meta:
        verbose_name = 'Öğrenci'
        verbose_name_plural = 'Öğrenciler'

    def __str__(self):
        return self.member.user.get_full_name()
