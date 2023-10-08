from django import forms
from admins.models import Book

class bookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

