from .models import Profile,Project
from django.forms import ModelForm
from django import forms

class PostForm(ModelForm):
    class Meta:
        model=Project
        field =('title'
        'description'
        'image'
        'url'
        'location'
        )





