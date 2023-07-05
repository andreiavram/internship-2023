
from django.contrib import admin

from todo.models import TaskItem, TaskUserRole, Document


class TaskRolesInline(admin.TabularInline):
    model = TaskUserRole
    extra = 1


class DocumentInline(admin.TabularInline):
    model = Document
    extra = 1


@admin.register(TaskItem)
class TaskItemAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "date_due"]
    autocomplete_fields = ["parent_task", "users"]
    search_fields = ["title", "description"]
    list_filter = ["parent_task"]

    inlines = [TaskRolesInline, DocumentInline]


