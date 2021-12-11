from .models import Profile,Project
from django.forms import ModelForm
from django import forms

class PostForm(ModelForm):
    class Meta:
        model=Project
        fields =('title',
        'description',
        'image',
        'url',
        'location',
        )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic', 'contact',)



