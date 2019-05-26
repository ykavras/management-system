from django.db import models


class Teacher(models.Model):
    type = models.CharField(verbose_name='Tip', max_length=16,
                            choices=(('Chief', 'Chief',), ('Coordinator', 'Coordinator')))
    user = models.OneToOneField('users.User', verbose_name='Kullanıcı', on_delete=models.PROTECT,
                                related_name='teacher')

    class Meta:
        verbose_name = 'Öğretmen'
        verbose_name_plural = 'Öğretmenler'

    def is_chief(self):
        return self.type == 'Chief'

    def __str__(self):
        return self.user.get_full_name()
