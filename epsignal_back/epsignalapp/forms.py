from django import forms
from .models import Contact , Problem

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone', 'email', 'subject', 'message']

class ProblemReportForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = ['problem_type', 'name', 'firstname', 'email', 'incident_date', 'description']

        # Customizing widgets for the fields
        widgets = {
            'problem_type': forms.Select(attrs={
                'id': 'problem-type', 
                'required': True
            }),
            'name': forms.TextInput(attrs={
                'id': 'name', 
                'required': True,
                'placeholder': 'Entrer votre nom'
            }),
            'firstname': forms.TextInput(attrs={
                'id': 'firstname', 
                'required': True,
                'placeholder': 'Entrer votre prénom'
            }),
            'email': forms.EmailInput(attrs={
                'id': 'email', 
                'required': True,
                'placeholder': 'youremail@example.com'
            }),
            'incident_date': forms.DateTimeInput(attrs={
                'id': 'formation', 
                'type': 'datetime-local',
                'required': True
            }),
            'description': forms.Textarea(attrs={
                'id': 'message', 
                'required': True,
                'placeholder': 'Décrivez le problème',
                'rows': 10
            })
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if any(char.isdigit() for char in name):
            raise forms.ValidationError("Le nom ne doit pas contenir de chiffres.")
        return name

    def clean_firstname(self):
        firstname = self.cleaned_data.get('firstname')
        if any(char.isdigit() for char in firstname):
            raise forms.ValidationError("Le prénom ne doit pas contenir de chiffres.")
        return firstname