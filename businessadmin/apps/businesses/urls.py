from django.urls import path
from .views import BusinessCreate, BusinessUpdate, BusinessDelete, BusinessDetail, BusinessList

app_name = 'business'

urlpatterns = [
    path('', BusinessList.as_view(), name='list'),
    path('olustur', BusinessCreate.as_view(), name='create'),
    path('<int:pk>/duzenle', BusinessUpdate.as_view(), name='edit'),
    path('<int:pk>/detay', BusinessDetail.as_view(), name='detail'),
    path('<int:pk>/sil', BusinessDelete.as_view(), name='delete'),
]
