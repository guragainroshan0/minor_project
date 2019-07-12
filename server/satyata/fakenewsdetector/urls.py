from django.urls import path
from . import views

urlpatterns = [
    path('<str:news>/<int:threshold>',views.index,name='index')
]