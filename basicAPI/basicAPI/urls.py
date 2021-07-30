from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('demo_1', include('demo_1.urls')),
    path('admin/', admin.site.urls),
]
