from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'^login/$', auth_views.login, name='login'),
    path(r'^logout/$', auth_views.logout, name='logout'),
]
