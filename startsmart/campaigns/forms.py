from django import forms
from .models import Campaign
from ..tags.models import Tags
class CampaignForm(forms.ModelForm):

    class Meta:
        model = Campaign
        fields = '__all__'

        widgets = {
                'creator': forms.TextInput(attrs={'value': '', 'id': 'element', 'type': 'hidden'})
            }

class TagsForm1(forms.ModelForm):
    # campaign = forms.ChoiceField(choices=Campaign.objects.all())

    def __init__(self, *args, **kwargs):
        super(TagsForm1, self).__init__(*args, **kwargs)

    class Meta:
        model = Tags
        fields = '__all__'

    name = forms.TextInput()
    campaigns = forms.ModelMultipleChoiceField(queryset=Campaign.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)