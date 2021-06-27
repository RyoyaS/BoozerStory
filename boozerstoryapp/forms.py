from django import forms

from .models import CommentModel

class CommentPostForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ('comment', 'story_id')