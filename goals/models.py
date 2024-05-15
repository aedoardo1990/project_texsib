from django.db import models
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords


class Goal(models.Model):
    """
    Goal model
    """
    CHOICES = [(i,i) for i in range(11)]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=255)
    title = models.TextField(blank=True)
    goal_description = models.TextField(blank=True)
    goal_criteria = models.TextField(blank=True)
    rating = models.IntegerField(max_length=10, choices=CHOICES)
    last_update = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    others = models.TextField(blank=True)
    history = HistoricalRecords()

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return f'{self.id} {self.title}'