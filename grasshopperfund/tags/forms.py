# from django import forms
#
# from .models import Tags
# from startsmart.campaigns.models import Campaign
#
# class TagsForm(forms.ModelForm):
#     # campaign = forms.ChoiceField(choices=Campaign.objects.all())
#
#     def __init__(self, *args, **kwargs):
#         super(TagsForm, self).__init__(*args, **kwargs)
#
#     class Meta:
#         model = Tags
#         fields = '__all__'
#
#     name = forms.TextInput()
#     campaigns = forms.ModelMultipleChoiceField(queryset=Campaign.objects.all(), widget=forms.CheckboxSelectMultiple)
#
#
