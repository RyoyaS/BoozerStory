from django import forms

from .models import CommentModel, StoryModel


class CommentPostForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ('comment', 'story_id')


class StoryPostForm(forms.ModelForm):
    class Meta:
        model = StoryModel
        fields = ('title', 'content', 'recommend_drink', 'author_id')
