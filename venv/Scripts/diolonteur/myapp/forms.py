from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = our_user
        fields = ['name', 'email', 'password', 'confirm_password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Паролі не співпадають")

        return cleaned_data

class PropositionForm(forms.Form):
    title = forms.CharField(max_length=50)
    proposition_text = forms.CharField(widget=forms.Textarea(attrs = {'cols': 60, 'rows':10}))
    cat = forms.ModelChoiceField(queryset=Category.objects.all())

class RequestForm(forms.Form):
    title = forms.CharField(max_length=50)
    request_text = forms.CharField(widget=forms.Textarea(attrs = {'cols': 60, 'rows':10}))
    cat = forms.ModelChoiceField(queryset=Category.objects.filter(id__gt=5))