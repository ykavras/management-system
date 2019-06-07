from django.urls import path
from .views import StudentCreate, StudentUpdate, StudentDelete, StudentDetail, StudentList

app_name = 'students'

urlpatterns = [
    path('', StudentList.as_view(), name='list'),
    path('olustur', StudentCreate.as_view(), name='create'),
    path('<int:pk>/duzenle', StudentUpdate.as_view(), name='edit'),
    path('<int:pk>/detay', StudentDetail.as_view(), name='detail'),
    path('<int:pk>/sil', StudentDelete.as_view(), name='delete'),
]
