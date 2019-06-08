from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import HttpResponse, get_object_or_404
from django.forms import model_to_dict
from django.utils.timezone import now

from openpyxl import Workbook

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


class ExportStudentView(View):
    def get(self, request, pk):
        teacher = get_object_or_404(Teacher, pk=pk)

        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="{}-ogretmenin-ogrenci-listesi_{}-{}-{}.xlsx"'.format(
            teacher.member.user.get_full_name(),
            now().day,
            now().month,
            now().year)
        wb = Workbook()
        ws = wb.active

        ws.append(['ADI', 'SOYADI', 'Okul Numarası', 'Sınıfı', 'İşletme', 'Staj Günleri'])
        fields = ['first_name', 'last_name', 'number', 'klass', 'business', 'days']

        for business in teacher.businesses.all():
            for item in business.scholarships.all():
                rows = []
                for field in fields:
                    if field == 'first_name':
                        rows.append(item.student.member.user.first_name)
                    elif field == 'last_name':
                        rows.append(item.student.member.user.last_name)
                    elif field == 'klass':
                        rows.append(item.student.klass.__str__())
                    elif field == 'business':
                        rows.append(item.business.name)
                    elif field == 'days':
                        rows.append(item.get_period_display())
                    else:
                        rows.append(item.student.number)
                ws.append(rows)
        wb.save(response)
        return response


class ExportBusinessView(View):
    def get(self, request, pk):
        teacher = get_object_or_404(Teacher, pk=pk)

        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="{}-ogretmenin-isletme-listesi_{}-{}-{}.xlsx"'.format(
            teacher.member.user.get_full_name(),
            now().day,
            now().month,
            now().year)
        wb = Workbook()
        ws = wb.active

        ws.append(['ADI', 'EMAIL', 'TEL', 'YETKİLİ', 'ADRES'])
        fields = ['name', 'email', 'phone', 'manager', 'address']

        for item in teacher.businesses.all():
            rows = []
            for field in fields:
                if field == 'manager':
                    rows.append(item.manager.user.get_full_name())
                else:
                    rows.append(model_to_dict(item).get(field))
            ws.append(rows)
        wb.save(response)
        return response
