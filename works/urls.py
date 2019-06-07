# works/urls.py

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from works import views

urlpatterns = [
    path('works/', views.WorkList.as_view(), name='work-list'),
    path('works/<int:pk>/', views.WorkDetail.as_view(), name='work-detail'),
   # path('', views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)