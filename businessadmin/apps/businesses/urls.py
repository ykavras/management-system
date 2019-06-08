from django.urls import path
from .views import *

app_name = 'business'

urlpatterns = [
    path('', BusinessList.as_view(), name='list'),
    path('olustur', BusinessCreate.as_view(), name='create'),
    path('<int:pk>/duzenle', BusinessUpdate.as_view(), name='edit'),
    path('<int:pk>/detay', BusinessDetail.as_view(), name='detail'),
    path('<int:pk>/sil', BusinessDelete.as_view(), name='delete'),
    path('<int:pk>/ogrenci-ihtiyaci', StudentQualificationCreate.as_view(), name='qualification_create'),
    path('<int:bs_pk>/ogrenci-ihtiyaci/<int:pk>/detay', StudentQualificationDetail.as_view(),
         name='qualification_detail'),
    path('<int:bs_pk>/ogrenci-ihtiyaci/<int:pk>/duzenle', StudentQualificationUpdate.as_view(),
         name='qualification_edit'),
    path('<int:bs_pk>/ogrenci-ihtiyaci/<int:pk>/sil', StudentQualificationDelete.as_view(),
         name='qualification_delete'),
    path('<int:pk>/ogrenci-gonder/', ScholarShipCreate.as_view(), name='scholarship'),
    path('liste-al', ExportBusinessView.as_view(), name='get_list'),
    path('ogrenci-listesi-al', ExportBusinessView.as_view(), name='get_student_list'),
    path('<int:pk>/ogrenci-listesi-al', ExportStudentView.as_view(), name='get_student_list'),
    path('<int:pk>/ogrencinin-dusunceleri/', StudentThoughtView.as_view(), name='student_thought'),
]
