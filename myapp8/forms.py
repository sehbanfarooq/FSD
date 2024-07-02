from django import forms
from myapp8.models import project
class project(forms.ModelForm):
    class Meta:
        model=project
        fields='_all_'