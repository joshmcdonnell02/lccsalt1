from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('userinfo/', views.userinfo, name='userinfo'),
    path('doctors/', views.doctorlist, name='doctors'),
    path('rooms/', views.roomlist, name='rooms'),
    path('patients/', views.patientlist, name='patients'),
]
