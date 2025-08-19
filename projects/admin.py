from django.contrib import admin
from . import models
from django.db.models import Count
from django.utils.translation import gettext_lazy as _

# Change the admin site title, header, and index title
admin.site.site_title = _('Project Management')
admin.site.site_header = _('Project Management Admin')
admin.site.index_title = _('Site Administration')


admin.site.register(models.Category)

@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'category', 'user', 'tasks_count')
    #list_per_page = 20
    list_select_related = ('category', 'user')
    list_editable = ('status',)

    def tasks_count(self, obj):
        return obj.tasks_count
    
    def get_queryset(self, request):
        query = super().get_queryset(request)
        query = query.annotate(tasks_count=Count('task'))
        return query


@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('description', 'is_completed', 'project')
    list_filter = ('is_completed', 'project')
    search_fields = ('description',)
    list_editable = ('is_completed',)