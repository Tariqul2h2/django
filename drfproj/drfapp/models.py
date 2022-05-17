from mailbox import NotEmptyError
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=200)
    ages = models.IntegerField()
    description = models.TextField
    dateEinroled = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name