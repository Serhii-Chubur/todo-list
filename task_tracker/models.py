from django.db import models


# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name='tasks')
    deadline = models.DateField()

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['is_done', '-created_at']
