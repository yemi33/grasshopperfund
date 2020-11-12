from django import forms

from .models import Organization, Post



class OrganizationForm(forms.ModelForm):

    class Meta:
        model = Organization
        fields = '__all__'

        widgets = {
                'owner': forms.TextInput(attrs={'value': '', 'id': 'element', 'type': 'hidden'})
            }



class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = [
            'author',
            'text',
        ]

        widgets = {
                'author': forms.TextInput(attrs={'value': '', 'id': 'post_author', 'type': 'hidden'}),
                # 'organization': forms.TextInput(attrs={'value': '', 'id': 'post_organization', 'type': 'hidden'}),
            }
