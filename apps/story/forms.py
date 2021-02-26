"""apps/story/forms.py"""

# Django modules
from django import forms

# My modules
from .models import Story, Comment

class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ('title', 'url')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)