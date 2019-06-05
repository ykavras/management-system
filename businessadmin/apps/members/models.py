from django.db import models


class Member(models.Model):
    types = (
        ('Chief', 'Chief'),
        ('Coordinator', 'Coordinator'),
        ('Student', 'Student'),
        ('Business', 'Business')
    )
    user = models.OneToOneField('users.User', verbose_name='Kullanıcı', on_delete=models.CASCADE,
                                related_name='member')
    type = models.CharField(max_length=15, verbose_name='Tip', choices=types)
    student = models.OneToOneField('students.Student', on_delete=models.CASCADE, related_name='member', null=True,
                                   blank=True)
    business = models.OneToOneField('business.Business', on_delete=models.CASCADE, related_name='member', null=True,
                                    blank=True)

    def __str__(self):
        return self.user.get_full_name()

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
