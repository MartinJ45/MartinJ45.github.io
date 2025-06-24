from django.urls import re_path, include
from Website.core import views

urlpatterns = [
    re_path(r'^$', views.HomeView.as_view(), name='home'),
]
