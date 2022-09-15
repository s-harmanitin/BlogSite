from django import forms
from .models import blog
from django.forms.widgets import TextInput,EmailInput,NumberInput,DateInput

class blogform(forms.ModelForm):
    class Meta:
        model = blog
        fields = "__all__"


        


