from django import forms

from .models import Tags

class TagsForm(forms.ModelForm):

    class Meta:
        model = Tags
        fields = '__all__'

        widgets = {
            'owner': forms.TextInput(attrs={'value': '', 'id': 'element', 'type': 'hidden'})
        }