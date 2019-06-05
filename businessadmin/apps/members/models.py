from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class Member(models.Model):
    types = (
        ('Chief', 'Chief'),
        ('Coordinator', 'Coordinator'),
        ('Student', 'Student'),
        ('Business', 'Business')
    )
    user = models.OneToOneField(User, verbose_name='Kullanıcı', on_delete=models.CASCADE,
                                related_name='member')
    type = models.CharField(max_length=15, verbose_name='Tip', choices=types)

    def __str__(self):
        return self.user.get_full_name() if self.user.get_full_name() else self.user.username

    class Meta:
        verbose_name = 'Kullanıcı'
        verbose_name_plural = 'Kullanıcılar'

    @property
    def is_cheif(self):
        return self.type == 'Chief'

    @property
    def is_coordinator(self):
        return self.type == 'Coordinator'

    @property
    def is_student(self):
        return self.type == 'Student'

    @property
    def is_business(self):
        return self.type == 'Business'

    @property
    def is_teacher(self):
        return self.is_coordinator or self.is_cheif
