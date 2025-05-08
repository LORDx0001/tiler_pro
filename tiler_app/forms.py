# forms.py
from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['first_name', 'last_name', 'email', 'phone', 'message']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'John'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Doe'}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'john.doe@example.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-input', 'placeholder': '07123 456789'}),
            'message': forms.Textarea(attrs={'class': 'form-textarea', 'placeholder': 'Tell us about your project...', 'rows': 5}),
        }