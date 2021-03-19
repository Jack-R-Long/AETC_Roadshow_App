from django.urls import path

from . import views

urlpatterns = [
    # /tool
    path('', views.index, name='index'),
]
