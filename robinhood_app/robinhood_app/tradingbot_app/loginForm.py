
from django import forms

class userNameForm(forms.Form):
    user_name = forms.CharField(label='userName', max_length=100)

class passwordForm(forms.Form):
    passWord = forms.CharField(label='password', max_length=100)

