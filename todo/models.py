from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import TextChoices


class TaskItem(models.Model):
    class TaskItemStatuses(TextChoices):
        PENDING = 1, "Pending"
        STARTED = 2, "Started"
        DONE = 3, "Done"

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_due = models.DateTimeField()

    users = models.ManyToManyField(get_user_model(), through="todo.TaskUserRole")
    parent_task = models.ForeignKey("todo.TaskItem", null=True, blank=True, on_delete=models.CASCADE, related_name="children")

    status = models.PositiveSmallIntegerField(choices=TaskItemStatuses.choices, default=TaskItemStatuses.PENDING)

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        ordering = ["-date_due"]

    def __str__(self):
        return f"{self.title}"


class Document(models.Model):
    uploaded_file = models.FileField(upload_to="documents")
    upload_time = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(get_user_model(), null=True, blank=True, on_delete=models.CASCADE)
    task = models.ForeignKey(TaskItem, on_delete=models.CASCADE, related_name="documents")



    def __str__(self):
        return f"File by {self.owner.username}"


class TaskUserRole(models.Model):
    class Roles(TextChoices):
        SUPERVISOR = "supervisor", "Supervisor"
        ASIGNEE = "assignee", "Assignee"
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    task = models.ForeignKey(TaskItem, on_delete=models.CASCADE)
    role = models.CharField(max_length=255, choices=Roles.choices, default=Roles.ASIGNEE)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField(null=True, blank=True)

