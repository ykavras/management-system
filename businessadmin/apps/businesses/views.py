from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import Business, StudentQualification
from ..members.models import Member
from ..teachers.models import Teacher

class BusinessCreate(PermissionRequiredMixin, CreateView):
    template_name = 'business_form.html'
    model = Business
    fields = ['name',
              'address',
              'email',
              'phone',
              'manager',
              'coordinator'
              ]

    def has_permission(self):
        return self.request.user.member.is_teacher

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['manager'].queryset = Member.objects.filter(type='Business')
        return form


class BusinessUpdate(PermissionRequiredMixin, UpdateView):
    template_name = 'business_form.html'
    model = Business
    fields = '__all__'

    def has_permission(self):
        return self.request.user.member.is_teacher


class BusinessDetail(DetailView):
    template_name = 'business_detail.html'
    model = Business


class BusinessDelete(DeleteView):
    template_name = 'business_form.html'
    model = Business
    success_url = reverse_lazy('business:list')


class BusinessList(ListView):
    template_name = 'business_list.html'
    model = Business


class StudentQualificationCreate(CreateView):
    model = StudentQualification
    template_name = 'student_qualification_form.html'
    fields = [
        'group',
        'period',
        'start_date',
        'finish_date',
        'piece',
        'branch',
        'qualifications',
    ]

    def form_valid(self, form):
        business_id = self.request.get_full_path().split('/')[2]
        try:
            form.instance.business = Business.objects.get(id=business_id)
        except:
            pass
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('business:detail', kwargs={'pk': self.object.business.pk})


class StudentQualificationUpdate(UpdateView):
    model = StudentQualification
    template_name = 'student_qualification_form.html'
    fields = [
        'group',
        'period',
        'start_date',
        'finish_date',
        'piece',
        'branch',
        'qualifications',
    ]

    def get_success_url(self):
        return reverse_lazy('business:detail', kwargs={'pk': self.object.business.pk})


class StudentQualificationDetail(DetailView):
    model = StudentQualification
    template_name = 'student_qualification_detail.html'
    fields = '__all__'


class StudentQualificationDelete(DeleteView):
    model = StudentQualification
    template_name = 'student_qualification_form.html'

    def get_success_url(self):
        return reverse_lazy('business:detail', kwargs={'pk': self.object.business.pk, })
