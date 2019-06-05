from django.db import models


class Student(models.Model):
    member = models.OneToOneField('members.Member', on_delete=models.PROTECT, related_name='student')
    number = models.PositiveIntegerField(verbose_name='Okul Numarası')
    term = models.ForeignKey('terms.Term', verbose_name='Dönem', on_delete=models.CASCADE, related_name='students')
    klass = models.ForeignKey('branchs.Klass', on_delete=models.CASCADE, related_name='students', verbose_name='Sınıf')

    class Meta:
        verbose_name = 'Öğrenci'
        verbose_name_plural = 'Öğrenciler'

    def __str__(self):
        return self.member.user.get_full_name()
