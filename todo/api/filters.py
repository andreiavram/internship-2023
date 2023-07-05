from django_filters import rest_framework as filters

from todo.models import TaskItem


class TaskFilter(filters.FilterSet):
    status = filters.ChoiceFilter(choices=TaskItem.TaskItemStatuses.choices)
    date_due = filters.DateFilter()


class DocumentFilter(filters.FilterSet):
    task = filters.ModelChoiceFilter(queryset=TaskItem.objects.filter(status=TaskItem.TaskItemStatuses.DONE))
