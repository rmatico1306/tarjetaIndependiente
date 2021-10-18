from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models 
from django.forms import fields
from django.forms.fields import EmailField
from django.forms.widgets import PasswordInput
from .models import *

class UserRegisterForm(UserCreationForm):
    email= forms.EmailField()
    password1=forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2=forms.CharField(label='Confirmar Contraseña',widget=forms.PasswordInput)
    class Meta:
        model= User
        fields=['username','email','password1','password2']
        help_texts= {k:"" for k in fields}
class TargetForm(forms.ModelForm):
    beneficiario= forms.IntegerField(widget= forms.HiddenInput())
    folio_tarjeta=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    beneficio=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model=Tarjeta
        fields=['folio_tarjeta','beneficio',]
    
    
