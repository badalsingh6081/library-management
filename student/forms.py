from django import forms
from django.contrib.auth.forms import AuthenticationForm,UsernameField


class student_form(forms.Form):
        name=forms.CharField(label='Full Name',widget=forms.TextInput(attrs={'class':'form-control fullname','placeholder':'Full Name'}))
        stu_id=forms.CharField(label='Student ID',widget=forms.TextInput(attrs={'class':'form-control student_id','placeholder':'Student ID'}))
        email=forms.CharField(label='Email',widget=forms.TextInput(attrs={'class':'form-control email','placeholder':'Email'}))
        password=forms.CharField(label='Password',widget=forms.TextInput(attrs={'class':'form-control password','placeholder':'Password'}))
        


class authenticationform(AuthenticationForm):
        username=UsernameField(widget=forms.TextInput(attrs={"autofocus": True,'class':'form-control username','placeholder':'Student ID'}))
        password = forms.CharField(
           label="Password",
           strip=False,
           widget=forms.PasswordInput(attrs={"autocomplete": "current-password",'class':'form-control password','placeholder':'Password'}),
    )