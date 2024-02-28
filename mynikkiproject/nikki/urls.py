from django.urls import path
from .views import NikkiList, NikkiDetail, NikkiCreate, NikkiUpdate, NikkiDelete, NikkiSearch

app_name = 'nikki'


urlpatterns = [
    path('nikki_list/', NikkiList.as_view(), name='nikki_list'),
    path('nikki_detail/<int:pk>/', NikkiDetail.as_view(), name='nikki_detail'),
    path('nikki_create/', NikkiCreate.as_view(), name='nikki_create'),
    path('nikki_update/<int:pk>/', NikkiUpdate.as_view(), name='nikki_update'),
    path('nikki_delete/<int:pk>/', NikkiDelete.as_view(), name='nikki_delete'),
    path('nikki_search/', NikkiSearch.as_view(), name='nikki_search'),
]