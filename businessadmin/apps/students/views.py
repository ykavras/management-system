from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import HttpResponse
from django.forms import model_to_dict
from django.utils.timezone import now

from openpyxl import Workbook

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
        user = self.request.user
        return user.is_authenticated and user.member.is_teacher

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
    template_name = 'student_create.html'
    pass


class StudentUpdate(StudentFormMixin, PermissionRequiredMixin, UpdateView):
    fields = [
        'number',
        'klass',
    ]

    def get_form(self, form_class=None):
        return super(UpdateView, self).get_form(form_class)


class StudentDetail(StudentFormMixin, PermissionRequiredMixin, DetailView):
    template_name = 'student_detail.html'
    model = Student


class StudentDelete(StudentFormMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'student_form.html'
    model = Student
    success_url = reverse_lazy('student:list')


class StudentList(StudentFormMixin, PermissionRequiredMixin, ListView):
    template_name = 'student_list.html'
    model = Student


class ExportView(StudentFormMixin, PermissionRequiredMixin, View):

    def get(self, request):

        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="ogrenci-listesi_{}-{}-{}.xlsx"'.format(
            now().day,
            now().month,
            now().year)
        wb = Workbook()
        ws = wb.active

        ws.append(['ADI', 'SOYADI', 'Okul Numarası', 'Sınıfı', 'İşletme', 'Kordinatör', 'Staj Günleri'])
        fields = ['first_name', 'last_name', 'number', 'klass', 'business', 'coordinator', 'days']
        last_term = Term.objects.last()
        for item in Student.objects.filter(term=last_term):
            rows = []
            for field in fields:
                if field == 'first_name':
                    rows.append(item.member.user.first_name)
                elif field == 'last_name':
                    rows.append(item.member.user.last_name)
                elif field == 'klass':
                    rows.append(item.klass.__str__())
                elif field == 'number':
                    rows.append(model_to_dict(item).get(field))
                else:
                    if hasattr(item, 'scholarship'):
                        if field == 'business':
                            rows.append(item.scholarship.business.name)
                        elif field == 'coordinator':
                            try:
                                rows.append(item.scholarship.business.coordinator.member.user.get_full_name())
                            except:
                                rows.append('')
                        elif field == 'days':
                            rows.append(item.scholarship.get_period_display())
                    else:
                        rows.append('')
            ws.append(rows)
        wb.save(response)
        return response
