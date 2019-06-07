from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import Student
from ..members.models import Member
from ..terms.models import Term


class StudentFormMixin:
    template_name = 'student_form.html'
    model = Student
    fields = [
        'member',
        'number',
        'klass',
    ]

    def has_permission(self):
        return self.request.user.member.is_teacher

    def form_valid(self, form):
        form.instance.term = Term.objects.last()
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['member'].queryset = Member.objects.filter(type='Student').exclude(id__in=
        Student.objects.values_list(
            'member__id', flat=True))
        return form


class StudentCreate(StudentFormMixin, PermissionRequiredMixin, CreateView):
    pass


class StudentUpdate(StudentFormMixin, PermissionRequiredMixin, UpdateView):
    fields = [
        'number',
        'klass',
    ]

    def get_form(self, form_class=None):
        return super(UpdateView, self).get_form(form_class)


class StudentDetail(DetailView):
    template_name = 'student_detail.html'
    model = Student


class StudentDelete(DeleteView):
    template_name = 'student_form.html'
    model = Student
    success_url = reverse_lazy('student:list')


class StudentList(ListView):
    template_name = 'student_list.html'
    model = Student
