from django.urls import path
from . import views

urlpatterns = [
    path('', views.vulnerability_list, name='vulnerability_list'),
]
