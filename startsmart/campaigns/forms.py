from django import forms
from .models import Campaign
from ..tags.models import Tags
class CampaignForm(forms.ModelForm):

    class Meta:
        model = Campaign
        fields = ['creator', 'title', 'description', 'target_money', 'days_left', 'image']

        widgets = {
                'creator': forms.TextInput(attrs={'value': '', 'id': 'element', 'type': 'hidden'})
            }

class TagsForm1(forms.ModelForm):
    # campaign = forms.ChoiceField(choices=Campaign.objects.all())

    def __init__(self, *args, **kwargs):
        super(TagsForm1, self).__init__(*args, **kwargs)
        if len(Tags.objects.all()) == 0: self.fields['tag'].help_text = 'No existing tags yet'
        else: self.fields['tag'].help_text = 'Existing tags you would like to include for your campaign'

    class Meta:
        model = Campaign
        fields = ['tag']

    enter_tags_you_would_like_to_include = \
        forms.CharField(max_length=200, help_text='A comma-separated or white-space separated list of tags.')
    tag = forms.ModelMultipleChoiceField(queryset=Tags.objects.all(), widget=forms.CheckboxSelectMultiple,
                                         required=False)