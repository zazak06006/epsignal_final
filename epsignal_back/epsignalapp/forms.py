from django import forms
from .models import Contact , Problem , Newsletter
from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'surname', 'email', 'subject', 'message']

class ProblemReportForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = ['problem_type','email', 'description']

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

class NewsletterForm(forms.ModelForm):
    class Meta:
        model =Newsletter
        fields = ['email']

