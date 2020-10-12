from django.forms import ModelForm


class CampaignForm(forms.ModelForm):

    class Meta:
        model = Campaign
        fields = '__all__'

        widgets = {
                'user': forms.TextInput(attrs={'value': '', 'id': 'element', 'type': 'hidden'})
            }
