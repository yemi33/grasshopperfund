from django import forms
from .models import Campaign, Donation
from ..tags.models import Tag
class CampaignForm(forms.ModelForm):

    class Meta:
        model = Campaign
        fields = ['creator', 'title', 'description', 'target_money', 'days_left', 'image']

        widgets = {
                'creator': forms.TextInput(attrs={'value': '', 'id': 'element', 'type': 'hidden'})
            }

class TagsForm(forms.ModelForm):
    # campaign = forms.ChoiceField(choices=Campaign.objects.all())

    def __init__(self, *args, **kwargs):
        super(TagsForm, self).__init__(*args, **kwargs)
        if len(Tag.objects.all()) == 0: self.fields['tag'].help_text = 'No existing tags yet'
        else: self.fields['tag'].help_text = 'Existing tags you would like to include for your campaign'

    class Meta:
        model = Campaign
        fields = ['tag']

    tag = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple,
                                         required=False)

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['campaign', 'amount', 'donor']

        widgets = {
            'campaign': forms.TextInput(attrs={'value': '', 'id': 'element', 'type': 'hidden'}),
            'donor': forms.TextInput(attrs={'value': '', 'id': 'element1', 'type': 'hidden'})
        }
