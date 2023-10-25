from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("convertido/", views.convertidof, views),
    path ("formato/", views.validar_formato)
    
]
