from django.urls import path
from . import views

urlpatterns = [
    path('<str:news>',views.index,name='index')
]