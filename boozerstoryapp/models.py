from django.db import models

#物語のモデル
class StoryModel(models.Model):
    title = models.CharField(max_length=100)#タイトル
    content = models.TextField()#本文
    recommend_drink = models.CharField(max_length=100)
    author_id = models.IntegerField(null=False, blank=False, default=0)

    def __str__(self):
        return self.title


class CommentModel(models.Model):
    comment = models.CharField(max_length=150)
    story_id = models.IntegerField(null=False, blank=False, default=0)

    def __str__(self):
        return self.comment
