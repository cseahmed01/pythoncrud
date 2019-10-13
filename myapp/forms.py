from django import forms
class LoginForms(forms.Form):
    username = forms.CharField(label='User Name', max_length=100)
    password = forms.CharField(label='Password', max_length=100)


class UserForm(forms.Form):
    name = forms.CharField(label='Name',max_length=100)
    phone = forms.CharField(label='Phone',max_length=100)
    email = forms.CharField(label='Email',max_length=100)
    address = forms.CharField(label='Address',max_length=100)
    description = forms.CharField(label='Description',max_length=100)


