from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth import get_user_model

from .models import Member
from .forms import MemberForm

User = get_user_model()


class MemberCreate(PermissionRequiredMixin, CreateView):
    template_name = 'member_form.html'
    form_class = MemberForm
    model = User

    def get_success_url(self):
        return reverse_lazy('member:detail', kwargs={'pk': self.object.pk})

    def has_permission(self):
        return self.request.user.member.is_teacher


class MemberUpdate(PermissionRequiredMixin, UpdateView):
    template_name = 'member_form.html'
    form_class = MemberForm
    model = User

    def get_success_url(self):
        return reverse_lazy('member:detail', kwargs={'pk': self.object.pk})

    def has_permission(self):
        return self.request.user.member.is_teacher


class MemberDetail(DetailView):
    template_name = 'member_detail.html'
    model = Member


class MemberDelete(DeleteView):
    template_name = 'member_form.html'
    model = User
    success_url = reverse_lazy('member:list')


class MemberList(ListView):
    template_name = 'member_list.html'
    model = User
