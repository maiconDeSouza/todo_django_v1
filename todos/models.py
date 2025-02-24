from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    completed = models.BooleanField(default=False, null=False, blank=False)

    def __str__(self):
        return self.title
