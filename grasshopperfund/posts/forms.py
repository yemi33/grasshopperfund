from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = [
            'author',
            'text',
        ]

        widgets = {
                'author': forms.TextInput(attrs={'value': '', 'id': 'post_author', 'type': 'hidden'}),
                # 'organEization': forms.TextInput(attrs={'value': '', 'id': 'post_organization', 'type': 'hidden'}),
            }
