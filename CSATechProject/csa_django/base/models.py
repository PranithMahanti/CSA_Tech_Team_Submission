from django.db import models
from django.contrib.auth.models import User

class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=500)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __list__(self):
        return [self.title, self.link, self.completed, self.created]

