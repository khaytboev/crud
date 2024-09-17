from django import forms
from .models import FirstModel


class FirstForm(forms.ModelForm):
    class Meta:
        model = FirstModel
        fields = [
            "title",
            "description",
        ]
