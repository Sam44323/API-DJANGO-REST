from django import forms
from django.forms import fields
from .models import User


class NewUser(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
