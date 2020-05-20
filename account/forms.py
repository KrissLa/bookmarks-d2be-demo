from django import forms

class LoginForm(forms.Form):
    """Форма входа"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
