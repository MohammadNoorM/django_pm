from django.db import models
from django.conf.global_settings import AUTH_USER_MODEL
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ProjectStatus(models.IntegerChoices):
    IN_PROGRESS = 1, "In Progress"
    COMPLETED = 2, "Completed"
    POSTPONED = 3, "Postponed"
    CANCELED = 4, "Canceled"


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.IntegerField(choices=ProjectStatus.choices, default=ProjectStatus.IN_PROGRESS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return self.title

class Task(models.Model):
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    Project = models.ForeignKey(Project, on_delete=models.CASCADE)