from django.urls import path
from . import views

urlpatterns = [
    path('<str:news>/<str:threshold>',views.index,name='index')
]