from django import forms
from .models import UserList

class UserForm(forms.ModelForm):
    class Meta:
        model =  UserList
        fields = '__all__'