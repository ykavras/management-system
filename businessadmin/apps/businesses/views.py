from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import HttpResponse, get_object_or_404
from django.forms import model_to_dict
from django.utils.timezone import now

from openpyxl import Workbook

from .models import Business, StudentQualification, ScholarShip
from ..members.models import Member
from ..students.models import Student


class BusinessPermissionMixin:

    def has_permission(self):
        user = self.request.user
        return user.is_authenticated and user.member.is_teacher


class BusinessCreate(BusinessPermissionMixin, PermissionRequiredMixin, CreateView):
    template_name = 'business_form.html'
    model = Business
    fields = ['name',
              'address',
              'email',
              'phone',
              'manager',
              'coordinator'
              ]

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['manager'].queryset = Member.objects.filter(type='Business')
        return form


class BusinessUpdate(BusinessPermissionMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'business_edited.html'
    model = Business
    fields = '__all__'


class BusinessDetail(BusinessPermissionMixin, PermissionRequiredMixin, DetailView):
    template_name = 'business_detail.html'
    model = Business


class BusinessDelete(BusinessPermissionMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'business_delete.html'
    model = Business
    success_url = reverse_lazy('business:list')


class BusinessList(BusinessPermissionMixin, PermissionRequiredMixin, ListView):
    template_name = 'business_list.html'
    model = Business


class StudentQualificationCreate(BusinessPermissionMixin, PermissionRequiredMixin, CreateView):
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


class StudentQualificationUpdate(BusinessPermissionMixin, PermissionRequiredMixin, UpdateView):
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


class StudentQualificationDetail(BusinessPermissionMixin, PermissionRequiredMixin, DetailView):
    model = StudentQualification
    template_name = 'student_qualification_detail.html'
    fields = '__all__'


class StudentQualificationDelete(BusinessPermissionMixin, PermissionRequiredMixin, DeleteView):
    model = StudentQualification
    template_name = 'student_qualification_form.html'

    def get_success_url(self):
        return reverse_lazy('business:detail', kwargs={'pk': self.object.business.pk, })


class ScholarShipCreate(PermissionRequiredMixin, CreateView):
    template_name = 'scholar_ship_form.html'
    model = ScholarShip
    fields = ['group', 'period', 'student']

    def form_valid(self, form):
        business_id = self.request.get_full_path().split('/')[2]
        try:
            form.instance.business = Business.objects.get(id=business_id)
        except:
            pass
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['student'].queryset = Student.objects.filter(scholarship__isnull=True)
        return form

    def get_success_url(self):
        return reverse_lazy('business:detail', kwargs={'pk': self.object.business.pk})

    def has_permission(self):
        user = self.request.user
        return user.is_authenticated and user.member.is_cheif


class ExportBusinessView(BusinessPermissionMixin, PermissionRequiredMixin, View):

    def get(self, request):
        businesses = Business.objects.filter(passive=False)

        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="isletme-listesi_{}-{}-{}.xlsx"'.format(
            now().day,
            now().month,
            now().year)
        wb = Workbook()
        ws = wb.active

        ws.append(['ADI', 'EMAIL', 'TEL', 'YETKİLİ', 'KORDINATOR', 'ADDRES'])
        FIELDS = ['name', 'email', 'phone', 'manager', 'coordinator', 'address', ]

        for item in businesses:
            rows = []
            for field in FIELDS:
                if field == 'manager' or field == 'coordinator':
                    id = model_to_dict(item).get(field)
                    rows.append(Member.objects.get(id=id).__str__()) if id else rows.append('')
                else:
                    rows.append(model_to_dict(item, fields=field).get(field))
            ws.append(rows)
        wb.save(response)
        return response


class StudentThoughtView(PermissionRequiredMixin, UpdateView):
    model = ScholarShip
    template_name = 'student_thoughts_form.html'
    fields = ['student_thoughts']
    success_url = '/'

    def has_permission(self):
        obj = self.request.user.member.student.scholarship
        user = self.request.user
        return user.is_authenticated and (user.member == obj.student.member)


class ExportStudentView(View):

    def get(self, request, pk):
        business = get_object_or_404(Business, pk=pk)

        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="{}_isletmesinin-ogrenci-listesi_{}-{}-{}.xlsx"'.format(
            business,
            now().day,
            now().month,
            now().year)
        wb = Workbook()
        ws = wb.active

        ws.append(['ADI', 'Okul Numarası', 'Sınıfı'])
        FIELDS = ['name', 'number', 'klass']

        for item in business.students.all():
            rows = []
            for field in FIELDS:
                if field == 'name':
                    rows.append(item.member.__str__())
                elif field == 'klass':
                    rows.append(item.klass.__str__())
                else:
                    rows.append(model_to_dict(item, fields=field).get(field))
            ws.append(rows)
        wb.save(response)
        return response
