from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.forms import model_to_dict
from django.utils.timezone import now

from openpyxl import Workbook

from .models import Business, StudentQualification
from ..members.models import Member
from ..students.models import Student


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


class ScholarShipView(View):

    def get(self, request, pk):
        students = Student.objects.filter(business__isnull=True)
        business = get_object_or_404(Business, pk=pk)
        return render(request, 'scholarship.html', {'students': students, 'business': business})

    def post(self, request, pk):
        students = self.request.POST.getlist('students')
        busines_id = self.request.POST.get('business')

        business = get_object_or_404(Business, id=busines_id)

        for id in students:
            try:
                student = Student.objects.get(id=int(id))
                student.business = business
                student.save()
            except:
                # TODO catch errors
                pass
        return redirect('business:detail', kwargs={'pk': busines_id})


class ExportBusinessView(View):

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
