from django.urls import path
from .views import BusinessCreate, BusinessUpdate, BusinessDelete, BusinessDetail, BusinessList, \
    StudentQualificationCreate, StudentQualificationUpdate, StudentQualificationDetail, StudentQualificationDelete

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
]
