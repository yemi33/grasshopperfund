from django import forms

from .models import Organization



class OrganizationForm(forms.ModelForm):

    class Meta:
        model = Organization
        fields = '__all__'
    
        widgets = {
                'owner': forms.TextInput(attrs={'value': '', 'id': 'element', 'type': 'hidden'})
            }
