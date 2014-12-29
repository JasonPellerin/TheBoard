from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from crew.models import Crew


class LoginForm(forms.Form):
        username        = forms.CharField(label=(u'User Name'))
        password        = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))
