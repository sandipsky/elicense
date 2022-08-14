from dataclasses import fields
from django import forms
from .models import *
from .widget import DatePickerInput, TimePickerInput, DateTimePickerInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class ApplicantForm(forms.ModelForm):
    class Meta:
        model = ApplicantInfo
        exclude = ('user',)
        widgets={
            'firstname' : forms.TextInput(attrs={'class':'text-input'}),
            'lastname' : forms.TextInput(attrs={'class':'text-input'}),
            'blood' : forms.Select(attrs={'class':'text-input'}),
            'phone' : forms.TextInput(attrs={'class':'text-input'}),
            'father' : forms.TextInput(attrs={'class':'text-input'}),
            'mother' : forms.TextInput(attrs={'class':'text-input'}),
            'citizenshipno' : forms.TextInput(attrs={'class':'text-input'}),
            'citizenshipdistrict' : forms.TextInput(attrs={'class':'text-input'}),
            'zone' : forms.TextInput(attrs={'class':'text-input'}),
            'district' : forms.TextInput(attrs={'class':'text-input'}),
            'ward' : forms.TextInput(attrs={'class':'text-input'}),
            'tole' : forms.TextInput(attrs={'class':'text-input'}),
            'dob' : DatePickerInput(),
            'citizenshipdate' : DatePickerInput(),
        }

class LicenseForm(forms.ModelForm):
    class Meta:
        model = License
        fields = ['category',]
        widgets={
            'category' : forms.Select(attrs={'class':'text-input'}),

        }
    
    def clean_category(self):
        category = self.cleaned_data.get("category")
        applicant = self.cleaned_data.get("applicant")
        votes = License.objects.filter(applicant=applicant, category=category).count()
        if votes >= 1:
            raise forms.ValidationError("You have already applied for this category")
        return category



class CreateUser(UserCreationForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={'class':'text-input', 'placeholder':'Enter your username'}),
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'text-input', 'placeholder':'Enter your password'}),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'text-input', 'placeholder':'Confirm password'}),
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username' , 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already taken")
        return username









