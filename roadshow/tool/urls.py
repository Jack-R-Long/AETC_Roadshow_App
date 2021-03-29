from django.urls import path

from . import views

urlpatterns = [
    # /tool
    path('old', views.old, name='old'),
    path('new', views.new, name='new'),
]
