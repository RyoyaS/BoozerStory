from django.contrib import admin
from .models import StoryModel,CommentModel

admin.site.register(StoryModel)
admin.site.register(CommentModel)
