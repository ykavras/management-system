from django.urls import path
from .views import *

app_name = 'students'

urlpatterns = [
    path('liste', TeacherList.as_view(), name='list'),
    path('olustur', TeacherCreate.as_view(), name='create'),
    path('<int:pk>/duzenle', TeacherUpdate.as_view(), name='edit'),
    path('<int:pk>/detay', TeacherDetail.as_view(), name='detail'),
    path('<int:pk>/sil', TeacherDelete.as_view(), name='delete'),
    path('<int:pk>/ogrenci-listesi', ExportStudentView.as_view(), name='get_student_list'),
    path('<int:pk>/isletme-listesi', ExportBusinessView.as_view(), name='get_business_list'),
]
