from django import forms
from .models import contactForm


class contact_Form(forms.ModelForm):
    class Meta:
        model = contactForm
        fields = ['username', 'passworld', 'email']
