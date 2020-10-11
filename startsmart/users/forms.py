from django.forms import ModelForm
from django import forms
from .models import Profile, Campaign

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

##Update part

class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['user', 'email', 'image']

        widgets = {
            'user': forms.TextInput(attrs={'value': '', 'id': 'element', 'type': 'hidden'})
        }

##Member choice members: (Free, Pro, Elite) or (Customer, Pro, Creator)
##MEMBER_CHOICES = [(), (), ()]

class CampaignForm(forms.ModelForm):

    class Meta:
        model = Campaign
        fields = '__all__'

