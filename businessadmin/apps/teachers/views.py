from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import Teacher
from ..members.models import Member
from ..terms.models import Term


class TeacherFormMixin:
    template_name = 'teacher_form.html'
    model = Teacher
    fields = [
        'member',
        'phone',
    ]

    def has_permission(self):
        return self.request.user.member.is_teacher

    def form_valid(self, form):
        form.instance.term = Term.objects.last()
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['member'].queryset = Member.objects.filter(type__in=['Chief', 'Coordinator']).exclude(id__in=
        Teacher.objects.values_list(
            'member__id', flat=True))
        return form


class TeacherCreate(TeacherFormMixin, PermissionRequiredMixin, CreateView):
    pass


class TeacherUpdate(TeacherFormMixin, PermissionRequiredMixin, UpdateView):
    fields = [
        'phone',
    ]

    def get_form(self, form_class=None):
        return super(UpdateView, self).get_form(form_class)


class TeacherDetail(DetailView):
    template_name = 'teacher_detail.html'
    model = Teacher


class TeacherDelete(DeleteView):
    template_name = 'teacher_form.html'
    model = Teacher
    success_url = reverse_lazy('teacher:list')


class TeacherList(ListView):
    template_name = 'teacher_list.html'
    model = Teacher
