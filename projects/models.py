from django.db import models
from django.conf.global_settings import AUTH_USER_MODEL
from django.utils.translation import gettext as _


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name
    
    


class ProjectStatus(models.IntegerChoices):
    IN_PROGRESS = 1, _("In Progress")
    COMPLETED = 2, _("Completed")
    POSTPONED = 3, _("Postponed")
    CANCELED = 4, _("Canceled")


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
    
    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')

class Task(models.Model):
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Task')
        verbose_name_plural = _('Tasks')

    class Meta:
        verbose_name = _("Task")
        verbose_name_plural = _("Tasks")

    def __str__(self):
        return self.description