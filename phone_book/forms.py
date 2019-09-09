from django import forms
from .models import PhoneBookModel


class PhoneBookForm(forms.ModelForm):
    class Meta:
        model = PhoneBookModel
        fields = '__all__'

