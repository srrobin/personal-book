from django import forms
from .models import DiaryModel


class DiaryForm(forms.ModelForm):
    class Meta:
        model = DiaryModel
        fields = '__all__'

    name = forms.CharField(label='Name',widget=forms.TextInput(attrs={'placeholder': ' Diary Title..'}))
    diary_text = forms.CharField(label='diary_text',widget=forms.Textarea(attrs={'placeholder': 'whats on your mind'}))
