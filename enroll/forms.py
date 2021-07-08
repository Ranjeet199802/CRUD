from django import forms
from .models import Registration


class regiform(forms.ModelForm):
    class Meta:
        model = Registration
        fields = "__all__"
