from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView

from todo.models import TaskItem

class TaskItemUserMixin:
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

class TaskListView(TaskItemUserMixin, LoginRequiredMixin, ListView):
    queryset = TaskItem.objects.all()

class TaskDetailView(TaskItemUserMixin, LoginRequiredMixin, DetailView):
    queryset = TaskItem.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bla'] = self.kwargs.get('bla')
        return context
