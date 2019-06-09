from django import forms
from django.contrib.auth import get_user_model

from .models import Member

User = get_user_model()

TYPES = ['Chief', 'Coordinator', 'Student', 'Business']


class MemberForm(forms.ModelForm):
    type = forms.ChoiceField(label='Tipi', choices=Member.types)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'password',
        ]

    def save(self, commit=True):
        type = self.cleaned_data.get('type')
        if type in TYPES:
            user = super().save(commit=False)
            if not user.pk:
                username = user.first_name[0] + user.last_name
                _username = username
                cntr = 0
                while True:
                    if not User.objects.filter(username=username).exists():
                        user.username = username
                        break
                    else:
                        cntr += 1
                        username = _username + str(cntr)
            if 'password' in self.changed_data:
                user.set_password(self.cleaned_data.get('password'))
            user.save()
            try:
                Member.objects.create(user=user, type=type)
            except:
                member = Member.objects.get(user=user)
                member.type = type
                member.save()
        return user
