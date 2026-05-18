from django.db import models

from django.conf import settings

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Tasks(models.Model):

    DIFFICULTY_CHOICES = [
        (1,'Easy'),
        (2, 'Medium'),
        (3, 'Hard')
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tasks'
        )
    
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(blank=True, null=True)
    difficulty = models.IntegerField(choices=DIFFICULTY_CHOICES)
    status = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)