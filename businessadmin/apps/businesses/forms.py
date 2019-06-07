from django import forms

from .models import Business
from ..members.models import Member


class BusinessForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(BusinessForm, self).__init__(*args, **kwargs)
        self.fields['manager'].queryset = Member.objects.filter(type='Business')

    class Meta:
        model = Business
        fields = '__all__'
