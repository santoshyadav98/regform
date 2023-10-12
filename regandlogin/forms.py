from django import forms
class Regform(forms.Form):
    firstName=forms.CharField(max_length=10)
    lastname=forms.CharField(max_length=10)
    email=forms.EmailField()
    username=forms.CharField(max_length=10)
    password=forms.IntegerField(max_value=10,widget=forms.PasswordInput())
    confpassword=forms.IntegerField(max_value=10,widget=forms.PasswordInput())

class loginform (forms.Form):
    username=forms.CharField(max_length=10)
    password=forms.CharField(max_length=10,widget=forms.PasswordInput())