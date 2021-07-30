from django.conf.urls import url
from demo_1 import views

urlpatterns = [
    url('', views.index, name="index"),
]
