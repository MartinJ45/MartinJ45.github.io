from django.urls import path, re_path, include
from Solver.core import views

urlpatterns = [
    re_path(r'^$', views.HomeView.as_view(), name='home'),
]
