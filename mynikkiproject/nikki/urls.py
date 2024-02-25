from django.urls import path
from .views import NikkiList, NikkiDetail, NikkiCreate

app_name = 'nikki'


urlpatterns = [
    path('nikki_list/', NikkiList.as_view(), name='nikki_list'),
    path('nikki_detail/<int:pk>/', NikkiDetail.as_view(), name='nikki_detail'),
    path('nikki_create/', NikkiCreate.as_view(), name='nikki_create'),
]