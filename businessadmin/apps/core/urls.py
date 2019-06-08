from django.urls import path
from .views import LoginView, HomeView, logout_view

app_name = 'core'

urlpatterns = [
    path('giris', LoginView.as_view(), name='login'),
    path('cikis', logout_view, name='logout'),
    path('', HomeView.as_view(), name='home'),
]
