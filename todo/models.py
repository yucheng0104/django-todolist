from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True)
    date_completed = models.DateTimeField(blank=True, null=True)
    important = models.BooleanField(default=False)
    # todo_id <=> user_id 外鍵關聯
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return F'[{self.created}] {self.title}-{self.user}'
