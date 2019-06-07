from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import Business


class BusinessCreate(PermissionRequiredMixin, CreateView):
    template_name = 'business_form.html'
    model = Business
    fields = ['name',
              'address',
              'email',
              'phone',
              'manager',
              ]

    def has_permission(self):
        return self.request.user.member.is_teacher


class BusinessUpdate(PermissionRequiredMixin, UpdateView):
    template_name = 'business_form.html'
    model = Business
    fields = '__all__'


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
