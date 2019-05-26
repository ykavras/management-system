from django.db import models


class Student(models.Model):
    user = models.OneToOneField('users.User', on_delete=models.CASCADE, related_name='student')

    class Meta:
        verbose_name = 'Öğrenci'
        verbose_name_plural = 'Öğrenciler'

    def __str__(self):
        return self.user.get_full_name()
