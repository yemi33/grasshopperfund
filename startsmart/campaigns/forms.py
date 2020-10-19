from django import forms
from .models import Campaign
class CampaignForm(forms.ModelForm):

    class Meta:
        model = Campaign
        fields = '__all__'

        widgets = {
                'creator': forms.TextInput(attrs={'value': '', 'id': 'element', 'type': 'hidden'})
            }
