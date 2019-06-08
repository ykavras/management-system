from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.views.generic import View


class HomeView(View):
    def get(self, request):
        payload = {
            'title': 'Ana sayfa'
        }
        return render(request, 'home.html', payload)


class LoginView(View):
    def get(self, request):
        payload = {
            'title': 'Giriş Yap'
        }
        return render(request, 'login.html', payload)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('core:home')
        else:
            messages.error('Giriş bilgileriniz doğrulanamadı')
            return redirect('core:login')


def logout_view(request):
    logout(request)
    return redirect('core:home')
