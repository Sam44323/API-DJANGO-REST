from django.conf.urls import url
from demo_1 import views

urlpatterns = [
    url('form', views.form_name_view, name="form_view"),
    url('', views.index, name="index"),
]
