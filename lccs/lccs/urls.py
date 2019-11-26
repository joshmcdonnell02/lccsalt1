from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', include('hospitalmanagementsystem.urls')),
]
