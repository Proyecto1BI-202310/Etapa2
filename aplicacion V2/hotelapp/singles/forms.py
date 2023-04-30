from django import forms
from .models import Single

class SingleModelForm(forms.ModelForm):
    class Meta:
        model = Single
        fields = ('texto',)