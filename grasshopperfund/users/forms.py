from django import forms
from .models import Profile
from ..tags.models import Tags

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['user', 'email', 'image']

        widgets = {
            'user': forms.TextInput(attrs={'value': '', 'id': 'element', 'type': 'hidden'})
        }

class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['user', 'email', 'image']

        widgets = {
            'user': forms.TextInput(attrs={'value': '', 'id': 'element', 'type': 'hidden'})
        }

class AddInterestedTagsForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['interested_tags']

    # interested tags should be prepopulated with check boxes
    interested_tags = forms.ModelMultipleChoiceField(
        queryset = Tags.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
