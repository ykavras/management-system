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
            'password',
            'first_name',
            'last_name',
            'email',
        ]

    def save(self, commit=True):
        type = self.cleaned_data.get('type')
        if type in TYPES:
            user = super().save(commit=True)
            user.set_password(self.cleaned_data.get('password'))
            try:
                Member.objects.create(user=user, type=type)
            except:
                member = Member.objects.get(user=user)
                member.type = type
                member.save()
        return user
