from django.db import models
from django.utils import timezone
from datetime import timedelta


# Create your models here.

class Questions(models.Model):
    question = models.CharField(max_length=200)
    pub_time = models.DateTimeField('Date Publish')

    def __str__(self) -> str:
        return self.question

    def was_published_recently(self):
        return self.pub_time >= timezone.now() - timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text
