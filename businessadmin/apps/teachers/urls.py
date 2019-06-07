from django.urls import path
from .views import TeacherCreate, TeacherUpdate, TeacherDelete, TeacherDetail, TeacherList

app_name = 'students'

urlpatterns = [
    path('liste', TeacherList.as_view(), name='list'),
    path('olustur', TeacherCreate.as_view(), name='create'),
    path('<int:pk>/duzenle', TeacherUpdate.as_view(), name='edit'),
    path('<int:pk>/detay', TeacherDetail.as_view(), name='detail'),
    path('<int:pk>/sil', TeacherDelete.as_view(), name='delete'),
]
