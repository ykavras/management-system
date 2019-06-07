from django.urls import path
from .views import MemberCreate, MemberUpdate, MemberDelete, MemberDetail, MemberList

app_name = 'members'

urlpatterns = [
    path('liste', MemberList.as_view(), name='list'),
    path('olustur', MemberCreate.as_view(), name='create'),
    path('<int:pk>/duzenle', MemberUpdate.as_view(), name='edit'),
    path('<int:pk>/detay', MemberDetail.as_view(), name='detail'),
    path('<int:pk>/sil', MemberDelete.as_view(), name='delete'),
]
